from django.shortcuts import render,get_object_or_404
from .forms import BrandForm
from .models import Brand
from django.http import HttpRequest, HttpResponse


# Create your views here.

def create_brand(request):
    if request.method == "POST":
        brands = BrandForm(request.POST, request.FILES)
        if brands.is_valid():
            brands.save()
    else:
        brands = BrandForm()
        print("GET request - rendering empty form")  

    return render(request, 'brands/create.html', {'brands': brands})



def brand_some(request:HttpRequest):
    brands = Brand.objects.all()[:8]
    return render(request, "brands/brandshows.html", {"brands" : brands})

def brand_page(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    return render(request, "brands/brand_details.html", {"brand": brand})