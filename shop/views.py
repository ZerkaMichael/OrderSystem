import uuid

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from cart.models import CartItem
from .models import Product


def home(request):
    return render(request, 'home.html')


def shop(request):
    if request.user.is_authenticated:
        # User is already logged in, redirect to shop page
        products = Product.objects.all()
        template = 'shop.html'

        # Get the number of items in the cart
        cart_items_count = CartItem.objects.filter(user=request.user).count()

        context = {
            'products': products,
            'cart_items_count': cart_items_count
        }

        return render(request, template, context)
    else:
        # User is not logged in, create new account and log in
        username = str(uuid.uuid4())[:8]
        print(username)
        password = User.objects.make_random_password()
        user = User.objects.create_user(username, password=password)
        user.save()
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('shop')
