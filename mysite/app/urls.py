from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('memmberlist/', views.memmberlist, name='memmberlist'),
    path('register/',views.register,name='register'),
    path('memmberlist/<int:pk>/', views.memmberdetail,name='memmberdetail'),
    path('editmemmber/<int:pk>/', views.editmemmber,name='editmemmber'),
    
    path('weeklyview/',views.weeklyview,name='weeklyview'),
    path('weeklyentry/',views.weeklyentry,name='weeklyentry'),
    path('updateweek/<int:pk>/',views.updateweek,name='updateweek'),

    path('loanview/',views.loanview,name='loanview'),
    path('giveloan/',views.giveloan,name='giveloan'),
    path('updatloan/<int:pk>/',views.updateloan,name='updateloan'),
    
    path('monthlyview/',views.monthlyview,name='monthlyview'),
    path('monthlyview/<str:date>/',views.monthlysummary,name='monthlysummary'),

    path('groupdetail/',views.groupdetail,name='groupdetail'),

    path('registeruser/',views.registeruser,name='registeruser'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('memmberprofile/',views.memmberprofile,name='memmberprofile'),

    path('createinterest/',views.createinterest,name='createinterest'),
    path('updateinterest/<int:pk>/<str:date>',views.updateinterest,name='updatein'),

]
    # path('monthlyreport',views.monthlyview,name='monthly'),
    
