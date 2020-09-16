from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.landing, name='landing'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)