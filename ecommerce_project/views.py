from datetime import timezone
from django.shortcuts import redirect, render
from products.models import Product

# show dashboard 
def Dashboard(request):
    
    return render (request,'dashboard.html')


# add product and its details
def add_product(request):
    if request.method=='POST':
        Name=request.POST.get('name')
        Description=request.POST.get('description')
        Price=request.POST.get('price')
        Category=request.POST.get('category')
        # print(Name,Description,Price,Category)

        product_add=Product(
            name=Name,
            description=Description,
            price=Price,
            category=Category

        )
        # save products in database
        product_add.save()
        return redirect ('view_products')
    Product_details=Product.objects.all()
    print(Product_details)
    context={
        'details':Product_details
    }
    return render(request,'dashboard.html',context)


def view_product(request):
    product_details=Product.objects.all()
    print(product_details)
    context={
        'product':product_details
    }
    return render (request,'view.html',context)
    

def edit_product(request,id):
    product_details=Product.objects.filter(id=id)
    context={
        'product':product_details
    }
    return render (request,'edit.html',context)

def update_product(request):
     if request.method=='POST':
        ide=request.POST.get('id')
        Name=request.POST.get('name')
        Description=request.POST.get('description')
        Price=request.POST.get('price')
        Category=request.POST.get('category')
        print(id,Name,Description,Price,Category)

        product_add = Product.objects.get(id=ide)
        product_add.name=Name
        product_add.description=Description
        product_add.price=Price
        product_add.category=Category
        print(product_add.name)
    
        product_add.save()
        return redirect ('view_products')
     return render(request,'edit.html')



def delete_product(request,id):
    delete_product=Product.objects.get(id=id)
    delete_product.delete()
    return redirect ('view_products')