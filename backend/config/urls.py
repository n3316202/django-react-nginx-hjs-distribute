from django.contrib import admin
from django.urls import path
from django.urls import path, include #dev_4

from .views import main_page  # dev_4
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  #dev_4
    path('', main_page, name='main'),  # 메인 페이지로 연결
]
