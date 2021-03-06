from django.urls import include, path
from rest_framework import routers
from . import views

from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'students', views.StudentsViewSet)
router.register(r'agents', views.AgentsViewSet)
router.register(r'uni', views.UniViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'service', views.ServiceViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', views.PostView.as_view(), name= 'posts_list'),
    # path('admin/', admin.site.urls),
    # path('api/', include('post.urls')),
]