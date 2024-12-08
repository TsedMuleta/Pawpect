from django.shortcuts import render
from rest_framework import viewsets
from .models import PetFood, Order
from .serializers import PetFoodSerializer, OrderSerializer

# PetFood API viewset
class PetFoodViewSet(viewsets.ModelViewSet):
    queryset = PetFood.objects.all()
    serializer_class = PetFoodSerializer

# Order API viewset
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import PetFood, Order

# Home page view
def home(request):
    return render(request, 'store/home.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Login view
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f"Username: {username}, Password: {password}")  # Check input data
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store:store')
        else:
            print("Invalid credentials")  # This will help debug
            return render(request, 'store/login.html', {'error': 'Invalid credentials'})
    return render(request, 'store/login.html')

# Logout view
def user_logout(request):
    logout(request)
    return redirect('store:home')

# Store view showing available pet food
@login_required
def store(request):
    pet_food_items = PetFood.objects.all()
    return render(request, 'store/store.html', {'pet_food_items': pet_food_items})

# Order view
@login_required
def place_order(request, food_id):
    pet_food = PetFood.objects.get(id=food_id)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        if quantity <= pet_food.stock:
            order = Order(user=request.user, pet_food=pet_food, quantity=quantity)
            pet_food.stock -= quantity
            pet_food.save()
            order.save()
            return redirect('store:order_success')
        else:
            return render(request, 'store/place_order.html', {'pet_food': pet_food, 'error': 'Not enough stock'})
    return render(request, 'store/place_order.html', {'pet_food': pet_food})

# Success page after placing an order
@login_required
def order_success(request):
    return render(request, 'store/order_success.html')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm

# Sign-up view
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            messages.success(request, f'Account created for {user.username}!')
            return redirect('store:home')  
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()  

    return render(request, 'store/signup.html', {'form': form})


# store/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('store:home')  # Redirect to home or any page after login
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

# store/views.py
from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('store:home')  # Redirect to home or any other page after logout


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import PetFood, Order
from django.contrib.auth.decorators import login_required
from decimal import Decimal

@login_required
def place_order(request, food_id):
    pet_food = get_object_or_404(PetFood, id=food_id)
    
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        
        try:
            # Ensure quantity is a valid integer
            quantity = int(quantity)
            
            # Validate that quantity is a positive number and doesn't exceed available stock
            if quantity <= 0:
                raise ValueError("Quantity must be greater than 0")
            
            if quantity > pet_food.stock:
                raise ValueError(f"Not enough stock available. Only {pet_food.stock} items left.")
            
            # Calculate total price using Decimal
            total_price = Decimal(pet_food.price) * Decimal(quantity)
            
            # Create the order
            order = Order(
                user=request.user,
                pet_food=pet_food,
                quantity=quantity,
                total_price=total_price
            )
            order.save()

            # Reduce the stock of the pet food item
            pet_food.stock -= quantity
            pet_food.save()
            
            # Add a success message to be displayed
            messages.success(request, f"Your order for {pet_food.name} has been placed successfully!")
            return redirect('store:order_success')
        
        except ValueError as e:
            # Handle invalid quantity input
            return render(request, 'store/place_order.html', {'pet_food': pet_food, 'error_message': str(e)})
        except Exception as e:
            # Handle any other errors, including decimal-related issues
            return render(request, 'store/place_order.html', {'pet_food': pet_food, 'error_message': "An error occurred: " + str(e)})

    return render(request, 'store/place_order.html', {'pet_food': pet_food})

from django.shortcuts import render
from .models import PetFood, Category

def store(request):
    categories = Category.objects.all()  # Get all categories
    pet_food_items = PetFood.objects.all()  # Get all pet food items

    # If a category is selected, filter by that category
    category_id = request.GET.get('category')
    if category_id:
        pet_food_items = pet_food_items.filter(category_id=category_id)

    return render(request, 'store/store.html', {'pet_food_items': pet_food_items, 'categories': categories})
