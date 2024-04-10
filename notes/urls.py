from django.urls import path

from notes.views import HomePageView, CreateNotaView, UpdateNoteView, DeleteNoteView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('new/', CreateNotaView.as_view(), name='new'),
    path('edit/<int:pk>', UpdateNoteView.as_view(), name='edit'),
    path('delete/<int:pk>', DeleteNoteView.as_view(), name='delete'),
]

