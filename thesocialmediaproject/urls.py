from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('users.api.urls')),
    path('post/', include('post.api.urls')),
]
