from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime

from django.views.decorators import csrf
from home.models import Contact
from django.contrib import messages
from .models import *
from django.http.response import JsonResponse
import json
import datetime
from .utils import cookieCart,cartData, guestOrder



def index(request):

    data =cartData(request)
    cartItems=data['cartItems']

    products = Product.objects.all()
    context = {'products' : products , 'cartItems' :cartItems}

    return render(request,'index.html',context)
    # return HttpResponse("this is home page")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("this is about page ")

def service(request):
    data =cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items =data['items']
        

    context ={'items':items , 'order' : order, 'cartItems':cartItems}
    return render(request,'service.html',context)
    # return HttpResponse("this is sevices page ")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your profile details updated.')

        # messages.success(request, 'Your message has been sent!')

    return render(request,'contact.html')
    # return HttpResponse("this is contact page ")    

def cart(request):

    data =cartData(request)

    cartItems=data['cartItems']
    order=data['order']
    items =data['items']


    context ={'items':items , 'order' : order ,'cartItems':cartItems}

    return render(request,'cart.html',context)
    # return HttpResponse("this is cart page ")

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer , complete=False)

    orderItem,created =  OrderItem.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action =='remove':
        orderItem.quantity = (orderItem.quantity -1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    print('Action:', action)
    print('productId:', productId)
    return JsonResponse('Item was added',safe=False)


# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data=json.loads(request.body)

    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
       

        
    else:
        customer,order=guestOrder(request,data)
        


    total=float(data['form']['total'])
    order.transaction_id=transaction_id

    if total==float(order.get_cart_total):
        order.complete=True
    order.save()


    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )
    return JsonResponse('Payment completed!',safe=False)
