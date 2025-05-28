from django.urls import path
from .views import HelloWorldView

#dev_4
urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello-world'),
]