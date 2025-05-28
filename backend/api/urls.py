from django.urls import include, path

# dev_5
from rest_framework import routers
from api.views import category_views
from api.views import hello_views


router = routers.DefaultRouter()
router.register("categories", category_views.CategoryViewSet)

#dev_4
urlpatterns = [
    path('hello/', hello_views.HelloWorldView.as_view(), name='hello-world'),
    path("", include(router.urls)),
]