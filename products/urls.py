from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductFormView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name="list_product"),
    path('agregar/', ProductFormView.as_view(), name="add_product")
]