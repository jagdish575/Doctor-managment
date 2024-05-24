from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path("", login, name="login"), 
    path('home/', index, name="home"),
    path('registration/', user_create, name="user_create"),
    path('signup/', signup, name="signup"),
    path('register/', register, name="register"),
    path('doctors/', doctor, name='doctors'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
