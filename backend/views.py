from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from backend.models import User, Admin, Interview_Authority, Interview, Question, Video, Performance, Train_Video

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












