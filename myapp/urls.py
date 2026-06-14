from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.loginTemp,name='loginTemp'),


    path('complaintView',views.complaintView,name='complaintView'),
    path('feedbackView',views.feedbackView,name='feedbackView'),
    path('blockView',views.blockView,name='blockView'),
    path('blockUser/<int:id>',views.blockUser,name='blockUser'),
    path('unblockUser/<int:id>', views.unblockUser, name='unblockUser'),
    path('replyView/<int:id>',views.replyView,name='replyView'),
    path('replySend', views.replySend, name='replySend'),
    path('verifyView', views.verifyView, name='verifyView'),
    path('acceptResearcher/<int:id>', views.acceptResearcher, name='acceptResearcher'),
    path('rejectResearcher/<int:id>', views.rejectResearcher, name='rejectResearcher'),
    path('registerationRView',views.registerationRView,name='registerationRView'),
    path('registerationRSend', views.registerationRSend, name='registerationRSend'),
    path('loginSend',views.loginSend, name='loginSend'),
    path('homeAView',views.homeAView, name='homeAView'),
    path('myprofileView', views.myprofileView, name='myprofileView'),
    path('passwordView', views.passwordView, name='passwordView'),
    path('uploadfindingsView', views.uploadfindingsView, name='uploadfindingsView'),
    path('loginTemp',views.loginTemp,name='loginTemp'),
    path('HomeRView',views.HomeRView, name='HomeRView'),
    path('updateprofile',views.updateprofile,name='updateprofile'),
    path('updateprofile',views.updateprofile,name='updateprofile'),
    path('updatepassword',views.updatepassword,name='updatepassword'),
    path('updatepassword',views.updatepassword,name='updatepassword'),
    path('viewfindings',views.viewfindings,name='viewfindings'),
    path('deletefindings/<int:id>',views.deletefindings,name='deletefindings'),
    path('uploadfindings_post',views.uploadfindings_post,name='uploadfindings_post'),
    path('registerview',views.registerview,name='registerview   '),
    path('uploaddetailsView',views.uploaddetailsView,name='uploaddetailsView'),
    path('uploaddetails', views.uploaddetails, name='uploaddetails'),
    path('viewdetails', views.viewdetails, name='viewdetails'),
    path('deletedetails/<id>', views.deletedetails, name='deletedetails'),
    path('editdetails/<id>', views.editdetails, name='editdetails'),
    path('editdetails_POST', views.editdetails_POST, name='editdetails_POST'),
    path('logout', views.logout, name='logout'),






    path('logincode',views.logincode,name='logincode'),
    path('scan',views.scan,name='scan'),
    path('registercode', views.registercode, name='registercode'),
    path('complaintcode', views.complaintcode, name='complaintcode'),
    path('complaintViewcode', views.complaintViewcode, name='complaintViewcode'),
    path('deletecomplaintcode', views.deletecomplaintcode, name='deletecomplaintcode'),
    path('feedbackcode', views.feedbackcode, name='feedbackcode'),
    path('feedbackViewcode', views.feedbackViewcode, name='feedbackViewcode'),
    path('feedbackViewcode', views.feedbackViewcode, name='feedbackViewcode'),
    path('updateprofilecode', views.updateprofilecode, name='updateprofilecode'),
    path('viewprofilecode', views.viewprofilecode, name='viewprofilecode'),
    path('editprofilecode', views.editprofilecode, name='editprofilecode'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('findingViewcode', views.findingViewcode, name='findingViewcode'),
    path('detailsViewcode', views.detailsViewcode, name='detailsViewcode'),
    path('researcherViewcode', views.researcherViewcode, name='researcherViewcode'),
    path('detailsViewcodeMore', views.detailsViewcodeMore, name='detailsViewcodeMore'),
    path('detailsViewcodeMore1', views.detailsViewcodeMore1, name='detailsViewcodeMore1'),
    path('chat_send', views.chat_send, name='chat_send'),
    path('chat_view', views.chat_view, name='chat_view'),
    path('chatwithuser', views.chatwithuser, name='chatwithuser'),
    path('chatview', views.chatview, name='chatview'),
    path('coun_msg/<int:id>', views.coun_msg, name='coun_msg'),
    path('coun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),
    path('machinelcode', views.machinelcode, name='machinelcode'),


]
