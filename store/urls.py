from django.contrib import admin
from django.urls import path, include
from core import views
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from .import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/all/', views.list_all_store),
    path('store/user/', views.list_user_store),
    path('store/detail/<id>', views.store_detail),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('store/register/', views.register_product),
    path('store/register/submit', views.set_product),
    path('store/delete/<id>', views.delete_product),
    path('', RedirectView.as_view(url='store/all/') ),
   
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


