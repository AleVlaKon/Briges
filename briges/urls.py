from django.urls import path

from .views import *


urlpatterns = [
    path('listbriges/', index, name='listbriges'),
    path('inputbrige/', input_brige_form, name='input_brige'),
    path('briges/<int:brige_id>/', brige)
]
