# from functools import total_ordering
# import imp
# from os import stat
# from calendar import c
# import re
# from tokenize import group
from django.forms import inlineformset_factory
from django.http import  HttpResponse
from django.shortcuts import redirect, render

from .decorators import notlogin ,allowedUsers ,ForAdmins
from .models import *
from .form import *
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import logout ,authenticate
from django.contrib.auth import login  as my_login
from django.contrib.auth.decorators import login_required 
import requests
from django.conf import settings
def home (req):
    # b=book.objects.all()
    # # return HttpResponse("this home views ")
    # return render(req,"main/login.html",{'boo':b})
    return render(req,"main/home.html")

    
@login_required(login_url='userlogin')
def about (req):
    return render(req,"main/login.html")
    # return HttpResponse("this about views ")



@login_required(login_url='userlogin')
@allowedUsers(['customerss'])
def profile (req,pk):
    cus=Customer.objects.get(id=pk)
    ord=cus.order_set.all()
    tord=ord.count()
    sfliter=OrderFilter(req.GET,queryset=ord)
    ord=sfliter.qs
    con={
        'cus':cus,
        'ord':ord,
        'tord':tord,
        'sfliter':sfliter,
    }

    return render(req,"main/profiles.html",con)
    # return HttpResponse("this contact views")
@login_required(login_url='userlogin')
def createid (req,pk):
    ords=inlineformset_factory(Customer,order,fields=('b','sstatus','t'),extra=1)
    cus=Customer.objects.get(id=pk)
    fs=ords(queryset=order.objects.none(),instance=cus)
    if req.method == "POST":
        # fs=ords(req.POST,)
        fs=ords(req.POST,instance=cus)
        if fs.is_valid():
            fs.save()
            return redirect('/customer')
    con={'fs':fs }

    return render(req,"main/createid.html",con)
@login_required(login_url='userlogin')
def create(req):
    ordf=Orderform()
    if req.method == "POST":
        # print (req.POST)
        fo=Orderform(req.POST)
        if fo.is_valid():
            fo.save()
            return redirect('/customer')
    con={'ordf':ordf}
    return render(req,"main/create.html",con)

@login_required(login_url='userlogin')
def update(req,pk):
    el=order.objects.get(id=pk)
    f=Orderform(instance=el)
    if req.method== "POST":
        f=Orderform(req.POST,instance=el)
        if f.is_valid():
            f.save()
            return redirect('/customer')
    con={'ordf':f}
    return render(req,'main/create.html',con)

@login_required(login_url='userlogin')
def delete(req,pk):
    ord=order.objects.get(id=pk)
    if req.method == 'POST':
        ord.delete()
        return redirect('/customer')
    con={'ord':ord}

    return render(req,'main/delete.html',con)




@login_required(login_url='userlogin')
@allowedUsers(allowgroups=['aadmins'])
def customer(req):
    cus=Customer.objects.all()
    ord=order.objects.all()
    tot_ord=ord.count()
    p_ord=ord.filter(sstatus='pending').count()
    d_ord=ord.filter(sstatus='delivered').count()
    inpg_ord=ord.filter(sstatus='inprograss').count()
    con={'custom':cus,
         'p_order':p_ord,
         'd_order':d_ord,
         'inprog':inpg_ord,
         'tot_order':tot_ord,
         'order':ord}
    return render(req,"main/custumers.html",con)



@notlogin
def register(req):
    form=CreateNewUser()
    if req.method=='POST':
        form=CreateNewUser(req.POST)
        if form.is_valid():
            # for recaptcha
            recaptcha_response=req.POST.get('g-recaptcha-response')
            data={
                'secret':settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response':recaptcha_response
            }
            r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
            reslt=r.json()
            if reslt['success']:
                #end recaptcha
                use=form.save()
                uname=form.cleaned_data.get('username')
                group=Group.objects.get(name='customerss')
                use.groups.add(group)

                messages.success(req,uname+' successfully created')
                return redirect('/userlogin')
            else:
                messages.error(req,'invalid recaptcha_response')

    con={'form':form}
    return render(req,"main/register.html",con)




@notlogin
def userlogin(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        password=req.POST.get('password1')
        user=authenticate(req,username= username,password=password) 
        if user is not None:
            my_login(req,user)

            # return profile(req.user.id)
            return redirect('/home')
        else:
            messages.info(req,"invalid login")
    con={}
    return render(req,"main/log.html",con)



@login_required(login_url='userlogin')
def userlogout(req):
    logout(req)
    return redirect('/customer')

@login_required(login_url='userlogin')
@allowedUsers(['customerss'])
def userpofile(req):
    ord=req.user.customer.order_set.all()

    tot_ord=ord.count()
    p_ord=ord.filter(sstatus='pending').count()
    d_ord=ord.filter(sstatus='delivered').count()
    inpg_ord=ord.filter(sstatus='inprograss').count()
    con={
         'p_order':p_ord,
         'd_order':d_ord,
         'inprog':inpg_ord,
         'tot_order':tot_ord,
         'ord':ord}

    # con={'ord':ord}
    return render(req,"main/userprofile.html",con)

@login_required(login_url='userlogin')
@allowedUsers(['customerss'])
def profile_info(req):
        # cus=req.user.customer
        # form=Customerform(instance=cus)
        # if re
        cus=req.user.customer
        f=Customerform(instance=cus)
        if req.method == "POST":
            f=Customerform(req.POST,req.FILES, instance=cus)
            if f.is_valid() :
                f.save()    
                
        con={'form':f}
        return render(req,"main/profile_info.html",con)