from django.shortcuts import render,redirect

from seller.models import Seller
from seller.models import Product


# Create your views here.

def sellerindex(request):
    return render(request,'sellerindex.html')
'''
def sellerlogin(request):
    return render(request,'sellerlogin.html')
'''

def sellerlogin(request):
    if request.method=='POST':
        try:
            Seller.objects.get(email=request.POST['email'])
            request.session['email']=request.POST['email']
            return redirect('sellerindex')
        except:
            return render(request,'sellerlogin.html',{'msg':'User not found'})
    return render(request,'sellerlogin.html')



def addproduct(request):
    sellerobj=Seller.objects.get(email=request.session['email'])
    if request.method=='POST':
        Product.objects.create(
            seller=sellerobj,
            name=request.POST['name'],
            des=request.POST['des'],
            price=request.POST['price'],
            quantity=request.POST['quantity'],
            discount=request.POST['discount'],
            pic=request.FILES['Pic']
        )
    return render(request,'addproduct.html')
    

def manageproduct(request):
    plist=Product.objects.all()
    return render(request,'manageproduct.html',{'productlist':plist})

def editproduct(request,pid):
    prodobj = Product.objects.get(id=pid)
    if request.method=='POST':
        if 'pic' in request.FILES:
            prodobj.name=request.POST['name']
            prodobj.des=request.POST['des']
            prodobj.price=request.POST['price']
            prodobj.quantity=request.POST['quantity']
            prodobj.discount=request.POST['discount']
            pic=request.FILES['Pic']
            prodobj.save()
            return redirect('manageproduct')
        else:
            prodobj.name=request.POST['name']
            prodobj.des=request.POST['des']
            prodobj.price=request.POST['price']
            prodobj.quantity=request.POST['quantity']
            prodobj.discount=request.POST['discount']
            prodobj.save()
            return redirect('manageproduct')
    return render(request,'editproduct.html',{'pobj':prodobj})

def deleteproduct(request,pid):
    prodobj = Product.objects.get(id=pid)
    if request.method=='POST':
        prodobj.delete()
        return redirect('manageproduct')
    return render(request,'deleteproduct.html',{'pobj':prodobj})