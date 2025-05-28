from django.urls import include, path
from .views import HelloWorldView


# dev_5
from rest_framework import routers
from .views import category_views

router = routers.DefaultRouter()
router.register("categories", category_views.CategoryViewSet)

#dev_4
urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello-world'),
    path("", include(router.urls)),
]