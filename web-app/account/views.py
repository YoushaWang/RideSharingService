from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserDetail,Ride
from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'index.html')

def signup(request):
    # return render(request,'signup.html')
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        tel=request.POST['tel']
        firstname=request.POST['first name']
        lastname=request.POST['last name']
        password=request.POST['password']
        password2=request.POST['password2']
        drive=request.POST.getlist('drive')
        license_num=request.POST['license_num']
        license_plate=request.POST['license_plate']
        car_brand=request.POST['car_brand']
        capacity=request.POST['capacity']

        car_type=request.POST['car_type']
        agree=request.POST.getlist('agree')
        if drive==["on"]:
            driver=True
        else:
            driver=False
            capacity=0
        if agree==["on"]:
            if password == password2:
                if User.objects.filter(email=email).exists():
                    messages.info(request,'Email has existed. Try again.')
                    return redirect("signup")
                elif User.objects.filter(username=username).exists():
                    messages.info(request,'Username has existed. Try again.')
                    return redirect("signup")
                else:
                    user=User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
                    user.save()
                    userDetail=UserDetail(username=user,drive=driver,email=email,tel=tel,first_name=firstname,last_name=lastname,password=password,license_num=license_num,license_plate=license_plate,car_brand=car_brand,capacity=capacity,car_type=car_type)
                    userDetail.save()
                    auth.login(request, user)
                    return redirect("main")
            else:
                messages.info(request,'Two passwords not matching')
                return redirect("signup")
        else:
            messages.info(request,'Please read Terms and Conditions')
            return redirect("signup")
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:#correct
            auth.login(request, user)
            # return HttpResponse("correct")
            return redirect("main")
        else:
            messages.info(request, 'Username or password wrong. Plz try again')
            return redirect("loginPage")
    else:
        return render(request, 'login.html')

@login_required(login_url='loginPage')
def logout(request):
    auth.logout(request)
    return redirect("loginPage")

@login_required(login_url='loginPage')
def main(request):
    return render(request,'main.html')

@login_required(login_url='loginPage')
def profile(request):
    curr=UserDetail.objects.filter(username=request.user).first()
    return render(request,'profile.html',{'curr':curr})

@login_required(login_url='loginPage')
def editprofile(request):
    # return render(request,'edit.html')
    if request.method == 'POST':
        curr=UserDetail.objects.filter(username=request.user).first()
        currUser=request.user
        #basic info
        username=curr.username
        email=request.POST['email']
        tel=request.POST['tel']
        first_name=request.POST['first name']
        last_name=request.POST['last name']
        #password
        password0=request.POST['password0']
        #   new password
        password=request.POST['password']
        #   comfirm password
        password2=request.POST['password2']
        #driver info
        drive=request.POST.getlist('drive')
        license_num=request.POST['license_num']
        license_plate=request.POST['license_plate']
        car_type=request.POST['car_type']
        car_brand=request.POST['car_brand']
        capacity=request.POST['capacity']
        if drive==["on"]:
            driver=True
        else:
            driver=False
        #basic info
        # curr.username=username
        curr.email=email
        curr.tel=tel
        curr.first_name=first_name
        curr.last_name=last_name
        #driver info
        curr.drive=driver
        curr.license_num=license_num
        curr.license_plate=license_plate
        curr.car_type=car_type
        curr.car_brand=car_brand
        curr.capacity=capacity
        #password info
        #if no old pwd: not to change it
        if password0 in [None, '']:
            if password or password2:
                messages.info(request,"Please enter old password first.")
                return redirect("editprofile")
        #if correct old pwd: change it
        elif password0==curr.password:
            if password==password2:
                # messages.info(request,"right")
                curr.password=password
                currUser.set_password(password)
            else:
                messages.info(request,"Two passwords not matching")
                return redirect("editprofile")
        #if wrong old pwd: error msg
        else:
            messages.info(request,"Old password not correct.Please try again.")
            return redirect("editprofile")
        curr.save()
        currUser.email=email
        currUser.first_name=first_name
        currUser.last_name=last_name
        currUser.save()
        messages.info(request,"Success!")
        return redirect("profile")
    else:
        curr=UserDetail.objects.filter(username=request.user).first()
        return render(request,'edit.html',{'curr':curr})

def terms_and_conditions(request):
    return render(request,'term.html')


@login_required(login_url='loginPage')
def rider_request_ride(request):
    if request.method == 'POST':
        owner = request.user
        rider_num=request.POST['rider_num']
        capacity=rider_num
        share=request.POST.getlist('share')
        if share==["on"]:
            ifshare=True
        else:
            ifshare=False
        pickup=request.POST['pickup']
        whereto=request.POST['whereto']
        schedule=request.POST['schedule']
        extraInfo=request.POST['extraInfo']
        car_type=request.POST['car_type']
        status="OPEN"
        ride=Ride(owner=owner,rider_num=rider_num,ifShare=ifshare,pickup=pickup,capacity=capacity,
            whereto=whereto, schedule=schedule,extraInfo=extraInfo,car_type=car_type,status=status)
        ride.save()
        messages.info(request,"Success!")
        return redirect("main")
    else:
        return render(request,'rider_request_ride.html')

@login_required(login_url='loginPage')
def driver_open_ride(request):
    curr=UserDetail.objects.filter(username=request.user).first()
    if curr.drive==False:
        messages.info(request,"You cannot access to driver's page")
        return redirect("main")
    else:
        if request.method == 'GET':
            # doing things here
            open_ride=Ride.objects.filter(status="OPEN",car_type=curr.car_type,capacity__lte=curr.capacity).all()
            return render(request,'driver_open_ride.html',{'open_ride':open_ride})

@login_required(login_url='loginPage')
def driver_confirmed_ride(request):
    curr=UserDetail.objects.filter(username=request.user).first()
    if curr.drive==False:
        messages.info(request,"You cannot access to driver's page")
        return redirect("main")
    else:
        if request.method == 'GET':
            comfirm_ride=Ride.objects.filter(status="COMFIRM",driver=curr).all()
            return render(request,'driver_confirmed_ride.html',{'comfirm_ride':comfirm_ride})


@login_required(login_url='loginPage')
def order_detail_pk(request,pk):
    r=Ride.objects.filter(id=pk).first()
    if request.method == 'POST':
        r.status="COMFIRM"
        r.driver=request.user.username
        r.save()
        messages.info(request,"Success!")
        send_mail(
            'Update msg for a ride',
            'your owning ride has been comfirmed by a driver',
            'temp_for_project@outlook.com',
            [r.owner.email],
            fail_silently=False,
            )
        # about share
        
        share_people = User.objects.filter(username=r.sharer).first()
        if share_people:
            send_mail(
                'Update msg for a ride',
                'your sharing ride has been comfirmed by a driver',
                'temp_for_project@outlook.com',
                [share_people.email],
                fail_silently=False,
                )   
        return render(request,'order_detail.html',{'r':r})
    else:
        return render(request,'order_detail.html',{'r':r})

        
@login_required(login_url='loginPage')
def order_detail_pk_edit(request,pk):
    r=Ride.objects.filter(id=pk).first()
    if request.method == 'POST':
        r.status="COMPLETE"
        r.save()
        messages.info(request,"Success!")
        return render(request,'order_detail_edit.html',{'r':r})
    else:
        return render(request,'order_detail_edit.html',{'r':r})