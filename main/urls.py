from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('seo', views.seo, name='seo'),
    path('research', views.research, name='research'),
    path('development', views.development, name='development'),
    path('branding', views.branding, name='branding'),
    path('smm', views.smm, name='smm'),
    path('optimization', views.optimization, name='optimization'),
    path('pr', views.pr, name='pr'),
    path('content_marketing', views.content_marketing, name='content_marketing')
]   