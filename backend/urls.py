from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='Login'),
    # path('question/',views.question,name='Question'),
    # path('submitURL/',views.submitURL,name='SubmitURL')
]