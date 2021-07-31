from django.urls import path
from . import views

urlpatterns = [
	path('dashboard/', views.index, name='dashboard-index'),
	
	path('staff/', views.staff, name='dashboard-staff'),
	path('staff/detail/<int:pk>/', views.staff_details, name='dashboard-staff-details'),

	path('order/', views.order, name='dashboard-order'),

	path('product/', views.product, name='dashboard-product'),
	# crud url
	path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'),
	path('product/update/<int:pk>/', views.product_update, name='dashboard-product-update'),
]