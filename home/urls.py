from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('bucket/', views.BucketHome.as_view(), name = 'bucket'),
    path('delete_bucket/<key>', views.DeleteBucketObjects.as_view(), name = 'delete_obj_bucket'),
    path('download_bucket/<key>', views.DownloadBucketObject.as_view(), name='delete_obj_bucket'),
    path('upload_bucket/', views.UploadBucketObject.as_view(), name = 'upload_bucket'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name = 'product_detail'),
]