from django.shortcuts import render
# from productcategory.models import ProductCategory
# from product.models import Product




def home_page(request):
    context = {
        'data' : 'data',
    }
    return render(request,'home_page.html',context)

def Header(request):
    context={}

    return  render(request,'layouts/header.html',context)

def Footer(request):
    context={}

    return  render(request,'layouts/footer.html',context)

# def product_slider_in_home_page(request):
#     categories = ProductCategory.objects.all()
#     products=[]
#     for category in categories:
#         products.append(Product.objects.filter(categories=category.id))
#     context={
#         'products':products
#     }
#     print(products)
#
#     return  render(request,'layouts/product_slider_in_home_page.html',context)