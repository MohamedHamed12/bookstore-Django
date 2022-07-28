from tokenize import group
from django.shortcuts import redirect
# from requests import request


def notlogin(veiwfun):
    def wrapper_fun(req,*args, **kwargs):
        if req.user.is_authenticated:
            return redirect ('/home')
        else:
            return veiwfun(req,*args,**kwargs)
    return wrapper_fun   

def allowedUsers(allowgroups=[]):
    def decorator(veiwfun):
        def wrapper_fun(req,*args, **kwargs):
            group=None
            if req.user.groups.exists(): 
                group=req.user.groups.all()[0].name
            if group in allowgroups:
                
                return veiwfun(req,*args,**kwargs)
            else:
                return redirect ('/home')
        return wrapper_fun
    return decorator
def ForAdmins(veiwfun):
    def wrapper_fun(req,*args, **kwargs):
        group=None
        if req.user.groubs.exists():
            group=req.user.groubs.all()[0].name
        if group=="aadmins":
            return veiwfun(req,*args,**kwargs)
        elif group=='customerss' :
            redirect('/about')   
        else: return  redirect('/home')
        

        # if req.user.is_authenticated:
        #     return veiwfun(req,*args,**kwargs)
        # else:
        #     return veiwfun(