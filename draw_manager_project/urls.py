from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from draw_manager_project import settings_dev, settings_common

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('draw_manager_app.urls')),
    path('accounts/', include('allauth.urls')),
]

#開発サーバーでメディアを配信できるようにする設定
urlpatterns += static(settings_common.MEDIA_URL,document_root=settings_dev.MEDIA_ROOT)