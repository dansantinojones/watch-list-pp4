from . import views
from django.urls import path


urlpatterns = [
    path(
        '', views.HomeView.as_view(), name='home'
        ),
    path(
        'media_list/', views.MediaList.as_view(), name='media_list'
        ),
    path(
        'list/recommend_box/', views.RecommendBoxView.as_view(), name='recommend_box'
        ),
    path(
        'add_media/', views.AddMedia.as_view(), name='add_media'
        ),
    path(
        'list/edit_media/<slug:slug>', views.EditMedia.as_view(), name='edit_media'
    ),
    path(
        'list/delete_media/<slug:slug>', views.DeleteMedia.as_view(), name='delete_media'
        ),
    path(
        'recommended/<slug:slug>', views.MediaRecommended.as_view(), name='media_recommended'
        ),
    path(
        '<slug:slug>/', views.MediaDetail.as_view(), name='media_detail'
        ),
]
