from django.contrib import messages
from django.shortcuts import render,redirect ,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import Category,video,User,watch_historys
from .forms import upload_form
# Create your views here.

def myfunctionc(request):
    return render(request,'index.html')
#signup
def signup(request):
    if request.method=='POST':
        username=request.POST['Uname']
        fname=request.POST['fname']
        Lname=request.POST['Lname']
        email=request.POST['email']
        passw=request.POST['password']
        pass2=request.POST['confirmPassword']

        #validations 
        if User.objects.filter(username=username):
            messages.error(request,"Username already exist")
            return render(request,'login.html')
        if User.objects.filter(email=email):
            messages.error(request,"Email already Exists")
            return render(request,'login.html')
        
        if passw!=pass2:
            messages.error(request,"Password Mismatch")
            return render(request,'login.html')

        myuser=User.objects.create_user(username,email,passw)
        myuser.first_name=fname
        myuser.last_name=Lname
        myuser.save()
        messages.success(request,"successfully Created")
        return redirect('signin')#loginform
    return render(request,'signup.html')
#sign_verification
def signin(request):
    if request.user.is_authenticated:
       return redirect('user_details')

    if request.method=='POST':
        user_name=request.POST['Uname']
        Password=request.POST['password']
        user=authenticate(username=user_name,password=Password)

        if user is not None :
            login(request,user)
            return render(request,'index.html')
        else:
            messages.error(request,"error")
            return redirect('signin')
    return render(request,'login.html')
#signout
@login_required
def signout(request):
    logout(request)
    messages.success(request,"loggedout successfully")
    return redirect('index')
#upload
@login_required
def video_load(request): #need to be defined
    #messages.clear(request)
    if not request.user.is_authenticated:
        return HttpResponse("You must be logged in to upload a video.", status=403)

    if request.method=='POST':
        form=upload_form(request.POST,request.FILES)
        if form.is_valid():
            video=form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('videoplay', pk=video.pk)
        else:
            return render(request, 'form.html', {'form': form})
    else:
        form=upload_form()
        return render(request,'form.html',{'form':form})
#account_details   
@login_required
def user_details(request):
    user_videos=video.objects.filter(user=request.user)
    watch_history=watch_historys.objects.filter(user=request.user).order_by('-History')
    return render(request,'user.html',{'videeo':user_videos,'history':watch_history}) # locate html for user details
#videocategory
@login_required
def video_category(request):
    category=Category.objects.all()
    x=video.objects.all()
    videos={}
    for categ in x:
        videos[categ]=video.objects.filter(user=request.user)
    return render(request, 'category.html',{'videos':videos})

def videoplay(request,pk):
    Videos = get_object_or_404(video, pk=pk)
    x=video.objects.all()
    return render(request, 'videos.html', {'video': Videos,'x':x})

def deletevideo(request,pk):
    if request.method=='POST':
        Video=get_object_or_404(video,pk=pk)
        
        if Video.user==request.user:
            Video.file.delete() 
            Video.delete()
            messages.success(request,"Deleted Sucessfuluy")
        else:
            messages.error(request,"User don't Have permisssion to delete")
    return redirect('user_details')

    
