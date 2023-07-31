from django.urls import path


from    .views import *


urlpatterns = [
    path('', MainListObject.as_view(), name='index'),
    path('archiveobjects', ArchiveListObject.as_view(), name='archive'),
    path('roadobject/<int:obj_id>/', RoadListObject.as_view(), name='roadobjectlist'),
    path('filterlistroads/', RoadIndexFilter.as_view(), name='filterlistroads'),
    path('listroads/', RoadIndex.as_view(), name='listroads'),
    path('inputroad/', InputRoad.as_view(), name='input_road'),
    path('<int:road_id>/', road)
]
