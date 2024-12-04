from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Category, Tour, ExploreMore,CardTour, Hotel

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def home_page(request):
    categories = Category.objects.all()
    tours = Tour.objects.all()[:2]
    explore_more = ExploreMore.objects.all()

    context = {
        'categories': categories,
        'tours': tours,
        'explore_more': explore_more
    }
    return render(request, "./home.html", context)


def category_tours(request, category_slug=None):
    categories = Category.objects.all()
    selected_category = category_slug or 'all'
    
    if selected_category == 'all':
        tours = Tour.objects.all()
    else:
        category = get_object_or_404(Category, slug=selected_category)
        tours = Tour.objects.filter(category=category)

    explore_more = ExploreMore.objects.all()

    context = {
        'categories': categories,
        'tours': tours,
        'explore_more': explore_more,
        'selected_category': selected_category,
    }
    return render(request, 'category_tours.html', context)



def search_action(request):
    query = request.GET.get('q', '')
    
    tours = Tour.objects.filter(name__icontains=query)
    
    explore_more = ExploreMore.objects.filter(name__icontains=query) | ExploreMore.objects.filter(location__icontains=query)
    
    context = {
        'query': query,
        'tours': tours,
        'explore_more': explore_more
    }
    
    return render(request, "search-results.html", context)


def tour_detail(request, tour_name):
    card = get_object_or_404(CardTour, name=tour_name)
    context = {
        'card': card,
        'gallery_images': card.get_gallery_images() 
    }
    return render(request, 'card.html', context)



def hotel_list(request, tour_id):
    card = get_object_or_404(CardTour, id=tour_id)
    hotels = Hotel.objects.filter(country=card.name) 
    
    context = {
        'hotels': hotels,
        'card': card
    }
    return render(request, 'hotels.html', context)



def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    gallery_images = hotel.images.all() 

    context = {
        'hotel': hotel,
        'gallery_images': gallery_images, 
    }
    return render(request, 'hotel_detail.html', context)



def logout_view(request):
    logout(request) 
    return redirect('login') 


def login_view(request):
    context = {}

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')  
            else:
                context['error'] = 'Invalid username or password.'
    else:
        form = LoginForm()

    context['form'] = form
    return render(request, 'login.html', context)

def register_view(request):
    context = {}

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            
            if User.objects.filter(username=username).exists():
                messages.error(request, "Пользователь с таким именем уже существует.")
                return redirect('register')

            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            return redirect('login') 

    else:
        form = RegistrationForm()

    context['form'] = form
    return render(request, 'register.html', context)

def account_info(request):
    user = request.user  
    context = {
        'user': user
    }
    return render(request, 'account_info.html', context)


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def office_location(request):
    return render(request, 'office_location.html')

def rating_view(request):
    return render(request, 'rating.html')





