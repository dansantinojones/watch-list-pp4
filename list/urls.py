from . import views
from django.urls import path


urlpatterns = [
    path('', views.MediaList.as_view(), name='home'),
    path('<slug:slug>/', views.MediaDetail.as_view(), name='media_detail'),
]