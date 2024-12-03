from django.shortcuts import render ,get_object_or_404 ,redirect
from django.http import HttpRequest, HttpResponse
from .forms import CarsForm
from cars.models import Cars , Color
from brands.models import Brand
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def views_home(request: HttpRequest):
    return render(request, 'main/home.html')


def all_views(request:HttpRequest):
    cars = Cars.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()

    brand_filter = request.GET.get('brand')
    color_filter = request.GET.get('color')
    search_query = request.GET.get('search')

    if brand_filter:
        cars = cars.filter(brand__id=brand_filter)
    if color_filter:
        cars = cars.filter(colors__id=color_filter)
    if search_query:
        cars = cars.filter(name__icontains=search_query)

    page_number = request.GET.get('page')
    paginator = Paginator(cars.distinct(), 8)
    cars_page = paginator.get_page(page_number)

    return render(request, 'main/all.html', {
        'cars': cars_page,
        'brands': brands,
        'colors': colors
    })

def create_views(request:HttpRequest):
    if request.method == "POST":
        cars = CarsForm(request.POST)
        if cars.is_valid():
            cars.save()
        messages.success(request, "Car Created successfully!")
    else:
        cars = CarsForm()  

    return render(request, 'main/create.html', {'cars': cars})


def car_detail_view(request: HttpRequest, car_id):
    car = get_object_or_404(Cars, id=car_id)
    return render(request, 'main/car_detail.html', {'car': car})


def car_update_view(request: HttpRequest, car_id):
    car = get_object_or_404(Cars, id=car_id)
    if request.method == "POST":
        form = CarsForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, "Car updated successfully!")
            return redirect('car_detail', car_id=car.id)
    else:
        form = CarsForm(instance=car)

    return render(request, 'main/car_form.html', {'form': form})

def car_delete_view(request: HttpRequest, car_id):
    car = get_object_or_404(Cars, id=car_id)
    if request.method == "POST":
        car.delete()
        messages.success(request, "Car deleted successfully!")
        return redirect('all_views')
    return render(request, 'cars/car_confirm_delete.html', {'car': car})

