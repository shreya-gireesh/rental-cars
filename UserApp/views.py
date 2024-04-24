from django.shortcuts import render, redirect
from datetime import datetime
from AdminApp.models import *
from UserApp.models import *

# Create your views here.
def home(request):
    cars = CarImgModel.objects.all()
    places = PlacesModel.objects.all()
    user_authenticated = 'user' in request.session
    username = request.session.get('user', None)
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('book-now'):
            request.session['pickup_location'] = request.POST.get('pickup_location')
            request.session['pickup_date'] = request.POST.get('pickup_date')
            request.session['dropoff_location'] = request.POST.get('dropoff_location')
            request.session['dropoff_date'] = request.POST.get('dropoff_date')
            return redirect('booking')
        if request.POST.get('loginbtn'):
            mailid = request.POST.get('mailid')
            pasw = request.POST.get('pasw')
            user = UserRegModel.objects.get(user_mail = mailid, user_pasw = pasw)
            request.session['user'] = user.user_name
            return redirect('/')
        if request.POST.get('regbtn'):
            uname = request.POST.get('uname')
            usermail = request.POST.get('usermail')
            upasw = request.POST.get('upasw')
            licenseno = request.POST.get('licenseno')
            newuser = UserRegModel()
            newuser.user_name = uname
            newuser.user_mail = usermail
            newuser.user_pasw = upasw
            newuser.license_no = licenseno
            newuser.save()
            return redirect('/')
    return render(request, 'home.html', {'cars': cars, 'user': user_authenticated, 'name': username, 'places': places})


def logout(request):
    del request.session['user']
    return redirect('/')


def booking(request):
    user_authenticated = 'user' in request.session
    username = request.session.get('user', None)
    pickup_loc = request.session.get('pickup_location')
    pickup_date = request.session.get('pickup_date')
    dropoff_loc = request.session.get('dropoff_location')
    dropoff_date = request.session.get('dropoff_date')

    pickup = PlacesModel.objects.filter(places_id = pickup_loc)
    dropoff = PlacesModel.objects.filter(places_id=dropoff_loc)

    # to find available cars
    car_id = BookingModel.objects.filter(pickup_date__lte=dropoff_date, dropof_date__gte=pickup_date).values_list(
        'car_id', flat=True)
    # booked_cars = CarImgModel.objects.exclude(car__car_id__in=car_id)
    # print(booked_cars)
    cars = CarImgModel.objects.all()

    # Convert the date strings to datetime objects
    pdate = datetime.strptime(pickup_date, '%Y-%m-%d')
    ddate = datetime.strptime(dropoff_date, '%Y-%m-%d')
    time_difference = ddate - pdate
    total_hours = time_difference.total_seconds() / 3600
    request.session['hour'] = total_hours

    if request.method == 'POST':
        # Filters
        if request.POST.get('filter-btn'):
            if request.POST.get('manual'):
                cars = cars.filter(car__car_type = 'Manual')
            if request.POST.get('automatic'):
                cars = cars.filter(car__car_type = 'Automatic')
            if request.POST.get('petrol'):
                cars = cars.filter(car__car_fuel = 'Petrol')
            if request.POST.get('diesel'):
                cars = cars.filter(car__car_fuel = 'Diesel')
            if request.POST.get('maruti'):
                cars = cars.filter(car__car_company = 'Maruti')
            if request.POST.get('toyota'):
                cars = cars.filter(car__car_company = 'Toyota')
            if request.POST.get('price') == '1':
                cars = cars.order_by('car__car_price')
            if request.POST.get('price') == '2':
                cars = cars.order_by('-car__car_price')

        # car-selection
        if request.POST.get('select-btn'):
            carid =  request.POST.get('carid')
            request.session['carid'] = carid
            return redirect('car')
    return render(request, 'booking.html', {'booked_cars': car_id, 'cars': cars, 'user': user_authenticated, 'name': username,
                                            'pickup':pickup, 'pickup_date':pdate.date(), 'dropoff':dropoff, 'dropoff_date':ddate.date()})


def blogs(request):
    user_authenticated = 'user' in request.session
    username = request.session.get('user', None)
    return render(request, 'blogs.html', {'user': user_authenticated, 'name': username})

def kochiblog(request):
    user_authenticated = 'user' in request.session
    username = request.session.get('user', None)
    return render(request, 'kochiblog.html', {'user': user_authenticated, 'name': username})

def tvmblog(request):
    user_authenticated = 'user' in request.session
    username = request.session.get('user', None)
    return render(request, 'tvmblog.html', {'user': user_authenticated, 'name': username})

def contact(request):
    user_authenticated = 'user' in request.session
    username = request.session.get('user', None)
    return render(request, 'contact.html', {'user': user_authenticated, 'name': username})

def about(request):
    user_authenticated = 'user' in request.session
    username = request.session.get('user', None)
    return render(request, 'about.html', {'user': user_authenticated, 'name': username})

def car(request):
    print('Car')

    pickup_loc = request.session.get('pickup_location')
    pickup_date = request.session.get('pickup_date')
    dropoff_loc = request.session.get('dropoff_location')
    dropoff_date = request.session.get('dropoff_date')
    hours = request.session.get('hour')

    pdate = datetime.strptime(pickup_date, '%Y-%m-%d')
    ddate = datetime.strptime(dropoff_date, '%Y-%m-%d')

    pickup = PlacesModel.objects.filter(places_id=pickup_loc)
    dropoff = PlacesModel.objects.filter(places_id=dropoff_loc)

    carid = request.session.get('carid')
    cars = CarImgModel.objects.filter(car_id = carid)
    car_interiors = CarInteriorsModel.objects.filter(car__car_id = carid)
    review = CommentModel.objects.filter(car__car_id = carid)
    user_authenticated = 'user' in request.session
    username = request.session.get('user', None)

    # if request.POST.get('confirm-btn'):
            # car_id = request.POST.get('car_id')
            # new_booking = BookingModel()
            # new_booking.car = CarModel.objects.get(car_id = car_id)
            # new_booking.user = UserRegModel.objects.get(user_name = username)
            # new_booking.pickup = request.session.get('pickup_location')
            # new_booking.pickup_date = request.session.get('pickup_date')
            # new_booking.dropof = request.session.get('dropoff_location')
            # new_booking.dropof_date = request.session.get('dropoff_date')
            # new_booking.save()
    return render(request, 'car.html', {'car_interiors': car_interiors, 'cars': cars, 'user': user_authenticated, 'name': username,
                                        'pickup':pickup, 'pickup_date':pdate.date(), 'dropoff':dropoff,
                                        'dropoff_date':ddate.date(), 'hours':hours, 'reviews':review})

def account(request):
    username = request.session.get('user')
    users = UserRegModel.objects.filter(user_name = username)
    completed_bookings = BookingModel.objects.filter(user__user_name=username, action=True)
    upcoming_bookings = BookingModel.objects.filter(user__user_name=username, action=False)
    return render(request, 'account.html', {'name': username, 'user': users, 'completed_bookings': completed_bookings, 'upcoming_bookings': upcoming_bookings })

def faq_section(request):
    return render(request, 'faq.html')