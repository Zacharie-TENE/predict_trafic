"""inventoryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user import views as user_views
from dashboard import views as dashboard_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('admin_login/', dashboard_views.login_admin, name='admin_login'),
    path('admin/login/', dashboard_views.loginadmin, name='adminlogin'),
    path('register/', user_views.register, name='user-register'),
    path('', dashboard_views.role_selection, name='role_selection'),
    path('', auth_views.LoginView.as_view(
        template_name='user/login.html'), name='user-login'),
    path('profile/', user_views.profile, name='user-profile'),
    path('profile/update/', user_views.profile_update,
         name='user-profile-update'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'),
         name='user-logout'),

    
    path('alertes_peremption/', dashboard_views.alertes_peremption, name='alertes_peremption'),
    path('login/',dashboard_views.LoginPage,name='login'),
    path('home/',dashboard_views.HomePage,name='home'),
    path('a_propos/', dashboard_views.a_propos, name='a_propos'),
    path('contact/',dashboard_views.contact,name='contact'),
    path('produits/',dashboard_views.produits,name='produits'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
