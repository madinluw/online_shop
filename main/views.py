from django.shortcuts import render
from .models import NewBalance, Images, Order, OrderItem
from django.http import HttpResponseRedirect
import uuid
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
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

@login_required(login_url='/sign_up/')
def cart(req, id):
    cart_products = req.session.get('cart_products', [])
    cart_products.append(id)
    st = set(cart_products)
    req.session['cart_products'] = list(st)
    nike = NewBalance.objects.all()
    context = {'Nike':nike}
    print(st)
    return render(req, 'index.html', context)

@login_required(login_url='/sign_up/')
def cart_page(req):
    cart_product = req.session.get('cart_products', [])
    cart_products = NewBalance.objects.filter(id__in = cart_product)
    total_price = 0
    for i in cart_products:
        total_price += i.price 
    context = {'product':cart_products, 'amount':cart_products.count(), 'total_price':total_price}
    return render(req, 'cart.html', context)

@login_required(login_url='/sign_up/')
def remove_from_cartpage(req,id):
    cart_products = req.session.get('cart_products', [])
    cart_products.remove(id)
    req.session['cart_products'] = cart_products
    return HttpResponseRedirect('/')

def about_us(req):
    info = req.session.get('info', [])
    context = {'info':info}
    return render(req, 'aboutus.html', context)

@login_required(login_url='/sign_up/')
def order(req):
    if req.method == 'POST':
        cart_product = req.session.get('cart_products', [])
        cart_products = NewBalance.objects.filter(id__in = cart_product)

        total_price = 0
        for i in cart_products:
            total_price += i.price 


        order = Order.objects.create(
        user = req.user,
        total_price = total_price,
        message = req.POST.get('message'),
        code = uuid.uuid4(),
        address = req.POST.get('address'),
        phone_number = req.POST.get('phone number'),
        )

        products = []
        for i in cart_products:
            item = OrderItem.objects.create(
                order = order,
                product = i
            )
            products.append(i.title)
        print(products)
        send_mail(
            f'Заказ от {req.user}',
            f'На адрес {req.POST.get("address")}\nНомер телефона: {req.POST.get("phone number")}\nCooбщение: {req.POST.get("message")}\nТовар: {", ".join(products)if len(products) > 1 else products[0]}',
            'from@example.com',
            ['muratbekovamadinaaa08@gmail.com'],
            fail_silently=False,
        )
        cart_products = req.session.get('cart_products', [])
        cart_products = []
        req.session['cart_products'] = cart_products
    return render(req, 'order.html')