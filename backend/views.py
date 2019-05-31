from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from backend.models import User, Admin, Interview_Authority, Interview, Question, Video, Performance, Train_Video
import cv2
import threading
import os
import urllib.request
import urllib.error
import time

http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
key = "rm8OknsE9biuRT2eVgWsSAHJNY2c-Xa3"
secret = "Gt0YAcdd9nU9yCAEnZ2S9edcJ5xIdqSI"

# Create your views here.
def login(request):
    obj = json.loads(request.body)
    name = obj['name']
    password = obj['password']
    interview_code = obj['interview_code']
    identity = obj['identity']
    res = {
        'loginMessage':''
    }
    try:
        if identity == 'user':
            user = User.objects.filter(user_name=name)
            userAuthority = Interview_Authority.objects.filter(name=name).first()
            if user.count()>0:
                if user[0].password == password:
                    uaObj = userAuthority.interview.all()
                    for ua in uaObj:
                        if ua.interview_code == interview_code:
                            res['loginMessage'] = 'success'
                            break
                        else:
                            res['loginMessage'] = 'not_authorized'
                else:
                    res['loginMessage'] = 'wrong_password'
            else:
                res['loginMessage']='no_user'
        elif identity == 'admin':
            admin = Admin.objects.filter(admin_name=name)
            adminAuthority = Interview_Authority.objects.filter(name=name).first()
            if admin.count() > 0:
                if admin[0].password == password:
                    uaObj = adminAuthority.interview.all()
                    for ua in uaObj:
                        if ua.interview_code == interview_code:
                            res['loginMessage'] = 'success'
                            break
                        else:
                            res['loginMessage'] = 'not_authorized'
                else:
                    res['loginMessage'] = 'wrong_password'
            else:
                res['loginMessage'] = 'no_user'
    except Exception as e:
        res = {
            'loginMessage':'error'
        }
    return HttpResponse(json.dumps(res),content_type='application/json')


def getQuestion(request):
    code = request.GET['content']
    try:
        questions = serializers.serialize("json", Question.objects.filter(interview__interview_code=code))
        res = {
            "code":200,
            "data": questions
        }
    except Exception as e:
        res = {
            "code":0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res),content_type="application/json")


def uploadVideo(request):
    try:
        file = request.FILES.get('video')
        # print(request.POST)
        interCode = request.POST.get('interview_code')
        interName = request.POST.get('name')
        # print(interCode)
        # print(interName)
        # print(file.name)
        # print(file.size)
        baseUrl = 'AI_Interview/video/'
        with open(baseUrl+file.name,'wb') as f:
            for line in file.chunks():
                f.write(line)
        res = {
            "code":200
        }
        t = threading.Thread(target=grabFrame,args=(1,file.name[:-5],baseUrl+file.name,interName,interCode))
        t.start()
        Video.objects.update_or_create(user_id=interName, defaults={'interview_code':interCode, 'url':baseUrl+file.name[:-5]+'.mp4', 'user_id':interName})
    except Exception as e:
        res = {
            "code":0
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


def getAffifnity(request):
    code = request.GET['content']
    try:
        performances = serializers.serialize("json", Performance.objects.filter(interview_code=code).order_by("-grade"))
        print(performances)
        res = {
            "code":200,
            "data": performances
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


# 取帧时间间隔
# 视频文件名
def grabFrame(timeInterval, fileName, videoPath, user, interview_code):
    # 转换格式
    code = "ffmpeg -i "
    codeMid = " -c:v copy "
    input = videoPath
    output = videoPath[:-5]+'.mp4'
    os.system(code+input+codeMid+output)
    os.remove(input)
    # 读取视频
    cap =cv2.VideoCapture(output)
    print(cap.isOpened())
    if(cap.isOpened()):
        # 获取总帧数
        frameCount=cap.get(cv2.CAP_PROP_FRAME_COUNT)
        print("总帧数：%d" %frameCount)
        # 获取帧率
        fps = cap.get(cv2.CAP_PROP_FPS)
        print("帧率：%d" %fps)
        os.mkdir("AI_Interview/frame/" + str(fileName))
        for i in range(1,int(frameCount/(fps*timeInterval))):
            # 设置帧的位置
            cap.set(cv2.CAP_PROP_POS_FRAMES,i*fps*timeInterval)
            # isRead 是否读取成功
            isRead, frame = cap.read()
            if isRead:
                cv2.imwrite("AI_Interview/frame/"+str(fileName)+"/"+str(i)+".jpg",frame)
        cap.release()
        print('grab frames done!')
        print('start call api')
        extractFeatures("AI_Interview/frame/" + str(fileName),user,interview_code)


# call api
def getFeatures(filepath):
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    fr = open(filepath, 'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
    data.append('1')
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
    data.append(
        "gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus")
    data.append('--%s--\r\n' % boundary)

    for i, d in enumerate(data):
        if isinstance(d, str):
            data[i] = d.encode('utf-8')

    http_body = b'\r\n'.join(data)

    # build http request
    req = urllib.request.Request(url=http_url, data=http_body)

    # header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)

    try:
        # post data to server
        resp = urllib.request.urlopen(req, timeout=5)
        # get response
        qrcont = resp.read()

        # if you want to load as json, you should decode first,
        # for example:
        data = json.loads(qrcont.decode('utf-8'))
        # print('result:  ' + str(qrcont.decode('utf-8')))
        if data['faces'] != []:
            attributes = data['faces'][0]['attributes']
            beauty = attributes['beauty']
            smile = attributes['smile']
            print('smile:  ' + str(smile))
            print('beauty:  ' + str(beauty))

            return beauty['female_score'], beauty['male_score'], smile['value']
        # save the answer to a file:
        # with open(filepath + '.txt', 'w', encoding='utf-8') as f:
        #     f.write(qrcont.decode('utf-8'))

    except urllib.error.HTTPError as e:
        print(e.read().decode('utf-8'))

def extractFeatures(framePath,user,interview_code):
    files = os.listdir(framePath)
    files.sort(key=lambda x: int(x[:-4]))
    featureList = []
    for path in files:
        filePath = os.path.join(framePath,path)
        print(filePath)
        featureList.append(getFeatures(filePath))
    beautyList=[]
    smile=0
    beauty=0
    count=0
    for feature in featureList:
        if feature[0]!=None and feature[1]!=None:
            beautyList.append((feature[0]+feature[1])/2)
        if feature[2]!=None:
            smile = smile+feature[2]
            count+=1
    beautyList.sort(reverse=True)
    if len(beautyList) == 0:
        beauty=0.0
    elif len(beautyList) == 1:
        beauty=beautyList[0]
    elif len(beautyList) == 2:
        beauty=beautyList[1]
    else:
        beauty = (beautyList[1]+beautyList[2])/2
    if count==0:
        smile=0.0
    else:
        smile = smile/count
    Video.objects.filter(interview_code=interview_code,user_id=user).update(beauty=beauty,smile=smile)




def linearRegression(interviewCode):
    x=[]
    y=[]
    tmpX = [] #临时存放样本
    tmpY = [] #临时存放标签
    trainVideo = Train_Video.objects.filter(interview_code=interviewCode)
    for tv in trainVideo:
        tmpX.append(tv.beauty)
        tmpX.append(tv.smile)
        tmpY.append(tv.affinity)
        x.append(tmpX)
        y.append(tmpY)
        tmpX=[]
        tmpY=[]
    lr = LinearRegression()
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=1)
    model = lr.fit(x_train,y_train)
    x_pred = []
    y_pred = []
    vUser = []
    video = Video.objects.filter(interview_code=interviewCode)
    for v in video:
        tmpX.append(v.beauty)
        tmpX.append(v.smile)
        vUser.append(v.user.user_name)
        x_pred.append(tmpX)
        tmpX=[]
    y_pred = lr.predict(x_pred)
    yLength = len(y_pred)
    for i in range(yLength):
        Performance.objects.filter(interview_code=interviewCode, user__user_name=vUser[i]).update(grade=y_pred[i])
