from django.urls import path
from app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('', views.home, name='home'),

	path('accounts/login/', auth_views.LoginView.as_view(template_name='login2.html')),

	path('importFromFile', views.importFromFile, name='importFromFile'),

	path('dashboard/', views.dashboard, name='dashboard'),
	path('charts-two/', views.charts_two, name='charts_two'),
	path('tables/', views.tables, name='tables'),
	path('forms/', views.forms, name='forms'),
	path('fix/', views.fix, name='fix'),

	path('charts/<slug:prob_type>', views.charts, name='charts'),
	
	path('empresa/<int:pk>', views.empresa, name='empresa'),


]