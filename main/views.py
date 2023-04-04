from django.shortcuts import render
from .models import NewBalance, Images
from django.http import HttpResponseRedirect
# Create your views here.

def main(req):
    nike = NewBalance.objects.all()
    context  = {'Nike':nike}
    return render(req, 'index.html', context)


def detail(req, id):
    product = NewBalance.objects.get(id=id)
    image = Images.objects.filter(sneakers=product)
    context = {'product':product, 'image':image}
    return render(req, 'detail.html', context)


def favorites(req, id):
    favorite_products = req.session.get('favorite_products', [])
    favorite_products.append(id)
    st = set(favorite_products)
    req.session['favorite_products'] = list(st)
    nike = NewBalance.objects.all()
    context = {'Nike':nike}
    print(st)
    return render(req, 'index.html', context)

def favorites_page(req):
    favorite_product = req.session.get('favorite_products', [])
    favorite_products = NewBalance.objects.filter(id__in = favorite_product)
    context = {'product':favorite_products}
    return render(req, 'favpage.html', context)

def remove_from_favpage(req,id):
    favorite_products = req.session.get('favorite_products', [])
    favorite_products.remove(id)
    req.session['favorite_products'] = favorite_products
    return HttpResponseRedirect('/')


def cart(req, id):
    cart_products = req.session.get('cart_products', [])
    cart_products.append(id)
    st = set(cart_products)
    req.session['cart_products'] = list(st)
    nike = NewBalance.objects.all()
    context = {'Nike':nike}
    print(st)
    return render(req, 'index.html', context)

def cart_page(req):
    cart_product = req.session.get('cart_products', [])
    cart_products = NewBalance.objects.filter(id__in = cart_product)
    context = {'product':cart_products}
    return render(req, 'cart.html', context)

def remove_from_cartpage(req,id):
    cart_products = req.session.get('cart_products', [])
    cart_products.remove(id)
    req.session['cart_products'] = cart_products
    return HttpResponseRedirect('/')

def about_us(req):
    info = req.session.get('info', [])
    context = {'info':info}
    return render(req, 'aboutus.html', context)
