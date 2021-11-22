from django.urls import path
from django.contrib import admin
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('castvote',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('update',views.update,name='update'),
    path('contact',views.contact,name='contact'),
    path('feedback',views.feedback,name='feedback'),
    path('candidates',views.candidates,name='candidates'),
    path('submitvote',views.submitvote,name='submitvote'),
    path('feedbacksubmit',views.feedbacksubmit,name='feedbacksubmit')
]