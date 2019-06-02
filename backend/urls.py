from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='Login'),
    path('question/',views.getQuestion,name='Question'),
    path('getAffinity/',views.getAffifnity,name="Affinity"),
    path('uploadVideo/',views.uploadVideo,name="Upload"),
    path('getTrain/',views.getTrain,name="Train"),
    path('setTrain/',views.setTrain,name="SetTrain"),
    path('admit/',views.admit,name="Admit"),
    path('getAdmit',views.getAdmit,name="GetAdimit")
    # path('submitURL/',views.submitURL,name='SubmitURL')
]