from django.urls import path,include
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('sign_up/',views.sign_up,name = 'sign_up'),
    path('login/',views.login_page,name = 'login_page'),
    path('logout/',views.logout_page,name = 'logout_page'),
    path('profile/',views.profile, name = 'profile'),
    path('update_profile/',views.update_profile,name = 'update_profile'),
    path('password/',views.password_change, name='password_change'),
    path('add_pro_pic/',views.add_pro_pic,name='add_pro_pic'),
    path('change_pro_pic/',views.change_pro_pic, name='change_pro_pic'),
]
