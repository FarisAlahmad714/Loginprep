#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # POST request for submitting a form for registr
    path('register', views.reg),
    # POST request for submitting a form for loggin
    path('success', views.success),
    path('login', views.login),
    # GET to render the success page after loggin/reg
    path('logout', views.logout),

]
