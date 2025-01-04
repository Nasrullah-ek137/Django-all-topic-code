from django.urls import path
from shanuapp1 import views

# bhai link aaise laga dekh  http://127.0.0.1:8000/django/ fir eski aage paste
#  karna jo urls likha hai vo

urlpatterns = [
    path('learn/',views.learn),
    path('code/',views.code),
    path('temp/',views.template),
    path('dynamic/',views.dynamic_temp),
    path('if/',views.if_stat),
    path('loop/',views.loop),
    path('static/',views.statics),
    path('',views.temp_home,name='homepg'),
    path('about/',views.temp_about,name='aboutpg'),
    path('course/',views.temp_courseinfo,name='courseinfo'),
    path('stu/',views.studentinfo),
    path('form/',views.showformdata),
    path('url/',views.dynamic_url1),
    path('url/<idd>',views.dynamic_url2),
    path('reg/',views.regi),
    path('set/',views.setcookie),
    path('get/',views.getcookie),
    path('del/',views.delcookie),
    path('sets/',views.setsession),
    path('gets/',views.getsession),
    path('dels/',views.delsession),
    path('mw/',views.m_home),
    path('qhome/',views.q_home),
    path('mhome/',views.model_home)




]
