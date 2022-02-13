from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sorting = sort_phones_check(request)
    if sorting:
        phone_obj = Phone.objects.all().order_by(sorting)
    else:
        phone_obj = Phone.objects.all()
    template = 'catalog.html'
    phone_dict = {}
    for phone in phone_obj:
        phone_dict[phone] = {
            'name': phone.name,
            'price': phone.price,
            'image': phone.image,
            'release_date': phone.release_date,
            'lte_exists': phone.lte_exists,
            'slug': phone.slug
        }
    context = {'phones': phone_dict}
    return render(request, template, context)

def show_product(request, slug):
    phone_obj = Phone.objects.filter(slug=slug)
    template = 'product.html'
    phone_dict = {}
    for phone in phone_obj:
        phone_dict = {
            'name': phone.name,
            'price': phone.price,
            'image': phone.image,
            'release_date': phone.release_date,
            'lte_exists': phone.lte_exists
        }
    context = {'phone': phone_dict}
    return render(request, template, context)

def sort_phones_check(request):
    sort_var = request.GET.get('sort')
    if not sort_var:
        return False
    elif sort_var == 'min_price':
        order_rule = 'price'
    elif sort_var == 'max_price':
        order_rule = '-price'
    elif sort_var == 'name':
        order_rule = 'name'
    return order_rule


