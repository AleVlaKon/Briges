from django.urls import path


from    .views import *


urlpatterns = [
    path('', road_index, name='index'),
    path('filterlistroads/', RoadIndexFilter.as_view(), name='filterlistroads'),
    path('listroads/', RoadIndex.as_view(), name='listroads'),
    path('inputroad/', input_road_form, name='input_road'),
    path('<int:road_id>/', road)
]
