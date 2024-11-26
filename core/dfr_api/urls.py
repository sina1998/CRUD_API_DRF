
from django.contrib import admin
from django.urls import path
from firstapp.views import userProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', userProfileView.as_view(), name="users"),
    path('profile/<id>/', userProfileView.as_view(), name="users"),
]
