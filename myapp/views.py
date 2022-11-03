from django.shortcuts import render,redirect

from myapp.models import *
from seller.models import *
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        try:
            User.objects.get(email=request.POST['email'])
            request.session['email']=request.POST['email']
            return redirect('index')
        except:
            return render(request,'login.html',{'msg':'user not found'})
    return render(request,'login.html')


def sproduct(request,pid):
    proj=Product.objects.get(id=pid)
    proj.discountedprice=proj.price-(proj.price*proj.discount/100)
    return render(request,'sproduct.html',{'proj':proj})

def allproduct(request):
    return render(request,'allproduct.html')

def hardware(request):
    plist=Product.objects.all()
    for item in plist:
        item.discountedprice=item.price-(item.price*item.discount/100)
    return render(request,'hardware.html',{'plist':plist})


def addtocart(request):
    pid=request.GET['pid']
    userobj= User.objects.get(email=request.session['email'])
    proj=Product.objects.get(id=pid)

    Cart.objects.create(
        product=proj,
        user=userobj,
        quantity=1

    )
    return JsonResponse({'msg':'Product Added To Cart'})

def cart(request):
    userobj= User.objects.get(email=request.session['email'])
    cartdata=Cart.objects.filter(user=userobj)
    carttotal=0
    for item in cartdata:
        item.product.discountedprice=item.product.price-(item.product.price*item.product.discount/100)
        carttotal += item.product.discountedprice
    return render(request,'cart.html',{'cartitems':cartdata,'carttotal':carttotal})


razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def checkout(request):
    userobj= User.objects.get(email=request.session['email'])
    orderobj=Order.objects.create(
        user=userobj,
        order_status='Confirm'
    )

    cartdata=Cart.objects.filter(user=userobj)
    s=0
    for i in cartdata:
        s += int(i.product.price)

    for item in cartdata:
        OrderDetails.objects.create(
            product=item.product,
            quantity=item.quantity,
            order=orderobj
        )

    
    currency = 'INR'
    amount = s*100  # Rs. 200
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url

    return render(request,'pay.html', context=context)


@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            #if result is not None:
            amount = context.razorpay_amount  # Rs. 200
            try:
 
                    # capture the payemt
                razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                return render(request, 'success.html')
            except:
 
                    # if there is an error while capturing payment.
                return render(request, 'fail.html')
            #else:
 
                # if signature verification fails.
                #return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()


def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'services.html')

