from django.urls import path

from .views import model_form_upload


urlpatterns = [
    path('', model_form_upload, name='file'),
]
