from django.shortcuts import render
from.models import *
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .utils import CategoriesMixin
# from django.http import HttpResponse


# def work(request):
    #create product
    # p = Product(title='Ford', price=2000)
    # p.save()
    # Product.objects.create(title='BMW', price=190000)

    #Get product
    # obj = Product.objects.all()
    # print(obj)
    

    # Update
    # obj = Product.objects.get(pk=1)
    # print(obj.price)

    # DELETE
    # obj = Product.objects.get(pk=1).delete
    # print(obj)

    # Получаем все обьекті кроме
    # obj = Product.objects.exclude(title='Range')
    # Filtr
    # obj=Product.objects.all().order_by('pk')

    # ПРоверяем кол-во

    # obj=Product.objects.filter(title='Ford').count()

    # Проверяем наличие
    # obj=Product.objects.filter(title='Ford').exists()

    # Проверяем больше te или равно>=
    # obj=Product.objects.filter(price__gte=10000)
    # Menwe<=
    # obj=Product.objects.filter(price__lte=10000)
# или
    # obj=Product.objects.filter(price__ln=(10000, 25000, 80000))

    # ТОчно
    # obj=Product.objects.filter(title__exact='Range Rover')
    # obj=Product.objects.filter(title__iexact='Range Rover')без регистра
    
    # Содержит
    # obj=Product.objects.filter(title__icontaince='Range Rover')без регистра 

    # One to many
    # o = Order.objects.select_related('product').get(pk=1)
    # MAny to Many
    # o = Product.objects.prefetch_related('categories').get(pk=1)
    
    # print(o)

    # return HttpResponse('Hello')


class HomeView(ListView, CategoriesMixin):
     model = Product
    
     def get_queryset(self):
        search_query = self.request.GET.get('search', None)
        if search_query:
            return self.model.objects.filter(
                Q(title__icontains=search_query)
                |
                Q(info__icontains=search_query)
        )        
        return Product.objects.all()
    

class ProductView(DetailView, CategoriesMixin):
     model = Product     


class CategoryView(DetailView, CategoriesMixin):
     model = Category


def save_order(request):
    categories = Category.objects.all()        
    order = Order()
    order.name = request.POST['user_name']
    order.email = request.POST['user_email']
    order.product = Product.objects.get(pk=request.POST['product_id'])
    order.save() 
    return render(
        request,
        'store/order.html',
        context={            
                'categories': categories,
                'order': order
            }
    )
