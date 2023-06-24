from django.urls import path

from .views import *


urlpatterns = [
    path('listbriges/', brige_index, name='listbriges'),
    path('inputbrige/', input_brige_form, name='input_brige'),
    path('<int:brige_id>/', brige)
]
