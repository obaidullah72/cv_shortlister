from django.urls import path
from .views import UploadCVView, FilterCVsView

urlpatterns = [
    path('upload/', UploadCVView.as_view(), name='upload_cv'),
    path('filter/', FilterCVsView.as_view(), name='filter_cvs'),
]
