from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .models import  Oekonomie
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Serializers define the API representation.
# class DataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Data
#         fields = ['income']
#
# # ViewSets define the view behavior.
# class DataViewSet(viewsets.ModelViewSet):
#     queryset = Data.objects.all()
#     serializer_class = DataSerializer

class OekonomieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oekonomie
        fields =['Jahr','Landkreis','BWSField','BIPField'] ##'__all__'  # (zeigt die id als Feld noch mit an)
        depth = 1

# ViewSets define the view behavior.
class OekonomieViewSet(viewsets.ModelViewSet):
    queryset = Oekonomie.objects.all()
    serializer_class = OekonomieSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'data', OekonomieViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    # path('', views.index, name='index'),
    # path('plist', views.post_list, name='post_list'),
    path('import', views.importData, name='import'),
    path('importOK', views.importOK, name='importOK'),
    path('dia', views.diagram, name='diagram'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
