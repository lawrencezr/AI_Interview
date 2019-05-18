from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers
from backend.models import User, Admin, Interview_Authority, Interview

# Create your views here.
def login(request):
    obj = json.loads(request.body)
    print(obj)
    name = obj['name']
    password = obj['password']
    interview_code = obj['interview_code']
    identity = obj['identity']
    # ifUserOrAdmin = 0 # 是否有用户
    # ifPassWordCorrect = 0 #密码是否正确
    # ifAuthorized = 0 # 是否被授权
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






