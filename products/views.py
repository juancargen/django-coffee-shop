from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductForm
from .models import Product

class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('list_product') #redirige a la url name: product_list

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/list_product.html'
    context_object_name = 'products'

'''
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        product_list = Product.objects.all()
        context['list_product'] = product_list
        return context
'''