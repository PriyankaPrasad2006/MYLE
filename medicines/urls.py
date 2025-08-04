from django.urls import path
from . import views

app_name = 'medicines'  # Namespace for URLs

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_medicine_qr, name='create_qr'),
    path('qr/<int:pk>/', views.qr_code_display, name='qr_code_display'),
    path('scanner/', views.qr_scanner, name='qr_scanner'),
    path('medicine/<str:batch_number>/', views.medicine_details_public, name='medicine_details_public'),
    path('test-qr/', views.qr_test_page, name='qr_test_page'),
    path('translate/', views.translate_medicine_info, name='translate_medicine_info'),
    path('list/', views.medicine_list, name='medicine_list'),
    path('download/<int:pk>/', views.download_qr_code, name='download_qr'),
    path('delete/<int:pk>/', views.delete_medicine, name='delete_medicine'),
    path('delete-all/', views.delete_all_medicines, name='delete_all_medicines'),
]
