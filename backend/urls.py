from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='Login'),
    path('question/',views.getQuestion,name='Question'),
    path('getAffinity/',views.getAffifnity,name="Affinity"),
    path('uploadVideo/',views.uploadVideo,name="Upload")
    # path('submitURL/',views.submitURL,name='SubmitURL')
]