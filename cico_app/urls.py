from django.urls import path
from . import views


urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/new/<int:pk>', views.event_new, name='event_new'),
    path('scan/', views.scan, name='scan'),
    path('person_list', views.person_list, name='person_list'),
    path('person/<int:pk>/edit', views.person_edit, name='person_edit'),
]