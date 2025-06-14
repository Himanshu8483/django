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


# def checkout(request):
#     cart = request.session.get('cart', {})
#     total = 0
#     for item in cart.values():
#         total += item['price'] * item['quantity']

#     return render(request, 'checkout.html', {'cart': cart, 'total': total})

import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

# Replace these with your actual Razorpay keys
RAZORPAY_KEY_ID = 'rzp_test_pr99iascS1WRtU'
RAZORPAY_KEY_SECRET = 'UTDIzPGwICnAssu3Q3lk7zUi'


client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

def checkout(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    amount_paise = int(total * 100)  # Razorpay works in paise

    if total > 0:
        payment = client.order.create({
            "amount": amount_paise,
            "currency": "INR",
            "payment_capture": "1"
        })

        context = {
            'cart': cart,
            'total': total,
            'razorpay_order_id': payment['id'],
            'razorpay_merchant_key': RAZORPAY_KEY_ID,
            'razorpay_amount': amount_paise,
            'currency': 'INR',
        }
        return render(request, 'checkout.html', context)
    else:
        return redirect('view_cart')


# @csrf_exempt
# def paymenthandler(request):
#     if request.method == "POST":
#         try:
#             payment_id = request.POST.get('razorpay_payment_id', '')
#             order_id = request.POST.get('razorpay_order_id', '')
#             signature = request.POST.get('razorpay_signature', '')

#             params_dict = {
#                 'razorpay_order_id': order_id,
#                 'razorpay_payment_id': payment_id,
#                 'razorpay_signature': signature
#             }

#             result = client.utility.verify_payment_signature(params_dict)

#             if result is None:
#                 # Payment success
#                 request.session['cart'] = {}  # clear cart
#                 return render(request, 'paymentsuccess.html')
#             else:
#                 return render(request, 'paymentfail.html')
#         except Exception as e:
#             return HttpResponseBadRequest()
#     else:
#         return HttpResponseBadRequest()
@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')

            params_dict = {
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # Correct: this raises an error if verification fails
            client.utility.verify_payment_signature(params_dict)

            # If successful
            request.session['cart'] = {}
            print("Payment ID:", payment_id)
            print("Order ID:", order_id)
            print("Signature:", signature)

            return render(request, 'paymentsuccess.html')

        except razorpay.errors.SignatureVerificationError:
            return render(request, 'paymentfail.html')
        except Exception as e:
            return HttpResponseBadRequest("Error: " + str(e))
    else:
        return HttpResponseBadRequest("Invalid request method")


# 4111 1111 1111 1111	Visa Card Test
# 5555 5555 5555 4444	 MasterCard Test

# pip install setuptools:   	Installs a tool to manage Python packages during installation and building. Required by many packages.
# pip install razorpay:     Installs the Razorpay SDK so you can use it in your code for payment integration.

