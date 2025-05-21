from django.shortcuts import render, redirect
from .models import Product
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', {})  # get cart from session (or empty)

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': product.price,
            'quantity': 1,
        }

    request.session['cart'] = cart  # save updated cart in session
    return redirect('view_cart')    # go to cart page


def view_cart(request):
    cart = request.session.get('cart', {})
    total = 0
    for item in cart.values():
        item['total_price'] = item['price'] * item['quantity']
        total += item['total_price']
    return render(request, 'cart.html', {'cart': cart, 'total': total})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]  # remove product from cart
    request.session['cart'] = cart
    return redirect('view_cart')


def clear_cart(request):
    request.session['cart'] = {}  # clear cart session
    return redirect('view_cart')


def checkout(request):
    cart = request.session.get('cart', {})
    total = 0
    for item in cart.values():
        total += item['price'] * item['quantity']

    return render(request, 'checkout.html', {'cart': cart, 'total': total})
