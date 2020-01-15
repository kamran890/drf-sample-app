from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_view 

urlpatterns = [
	path('', views.home, name='home'),
	path(r'register/', views.signup, name='signup'),
	path('login/', auth_view.LoginView.as_view(), name='login'),
	path('logout/', auth_view.LogoutView.as_view(), name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)