from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from shop.models import Section, Product


def index(request):

    products = Product.objects.all().order_by(get_order_by_products(request))[:8]
    context = {'products': products}
    return render(
        request,
        'index.html',
        context=context
    )

def get_order_by_products(request):
    order_by = ''
    if request.GET.__contains__('sort') and request.GET.__contains__('up'):
        sort = request.GET['sort']
        up = request.GET['up']
        if sort == "price" or sort == 'title':
            if up == '0':
                order_by = '-'
            order_by += sort
    if not order_by:
        order_by = '-date'
    return order_by

def delivery(request):
    return render(
        request,
        'delivery.html',
    )

def contacts(request):
    return render(
        request,
        'contacts.html',
    )

def section(request, id):
    #obj = Section.objects.get(pk=id)
    obj = get_object_or_404(Section, pk=id)
    products = Product.objects.filter(section__exact=obj).order_by(get_order_by_products(request))
    context ={'section': obj, 'products': products}
    return render(
        request,
        'section.html',
        context=context
    )


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.\
                                  filter(section__exact=self.get_object().section).\
                                  exclude(id=self.get_object().id).order_by('?')[:4]
        return context


def handler404(request, exception):
    return render(request, '404.html', status=404)