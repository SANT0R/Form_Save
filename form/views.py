from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import * # formlar
from django.contrib.auth.decorators import * #görünüm gizlenme
from django.http import * # Http komutları
from .models import form
import secrets 
# Create your views here.


    
def add(request):
    if request.method == "GET":
        
        return render(request,"Add.html")
    else:
        title = request.POST.get("title")
        explonation = request.POST.get("explonation")
        link = request.POST.get("link")
        email = request.POST.get("email")
        photo = request.POST.get("photo")

        codes = form.objects.filter(save_code__isnull=False)
        savecode = ""
        while savecode == "":
            savecode = secrets.token_hex(nbytes=32)
            for code in codes:
                if savecode == code.getsavecode:
                    savecode = ""
                
        newForm = form(save_code = savecode, title = title, explonation = explonation, link = link, email = email, photo = photo )
        newForm.save()
        
        context={
                "savecode":savecode,
            }
        return render(request,"Add.html",context)

def search(request):
    
    return render(request,'search.html')

def showform(request):

    code = request.POST.get("code")
    theForm = get_object_or_404(form, save_code = code)
    if theForm == None:
        context={}
    else:
        context={
                "theForm":theForm,
                "title":theForm.title,
                "explonation":theForm.explonation,
                "link":theForm.link,
                "email":theForm.email,
                "photo":theForm.photo,
            }
    return render(request,'showform.html',context)
