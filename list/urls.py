from . import views
from django.urls import path


urlpatterns = [
    path('', views.MediaList.as_view(), name='home'),
    path('add_media/', views.AddMedia.as_view(), name='add_media'),
    path('recommended/<slug:slug>', views.MediaRecommended.as_view(), name='media_recommended'),
    path('<slug:slug>/', views.MediaDetail.as_view(), name='media_detail'),
]