from django.shortcuts import render, redirect
from .models import Tutorial,TutorialCategory,TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login 
from django.contrib import messages
from .forms import NewUserForm
from django.http import HttpResponse
# Create your views here.
def single_slug(request,single_slug):
    categories = [c.slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        #return HttpResponse(f"{single_slug} is a category")
        matching_series=TutorialSeries.objects.filter(category__slug=single_slug)

        series_urls={}
        for m in matching_series.all():
            part_one=Tutorial.objects.filter(series__series=m.series).earliest('published')
            series_urls[m]=part_one.slug  

        return render(request,'main/category.html',{'part_ones':series_urls})    

    tutorials = [t.slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        #return HttpResponse(f"{single_slug} is a Tutorial")
        this_tutorial=Tutorial.objects.get(slug=single_slug)
        tutorial_from_series=Tutorial.objects.filter(series__series=this_tutorial.series).order_by('published')
        this_tutorial_idx=list(tutorial_from_series).index(this_tutorial)
        #print(this_tutorial_idx)

        return render(request,
                       "main/tutorial.html",
                      {"tutorial":this_tutorial,
                       "sidebar":tutorial_from_series,
                       "this_tutorial_idx":this_tutorial_idx})

    return HttpResponse(f"{single_slug} does not correspond to anything we know of!")

def intro(request):
    return render(request = request,
                  template_name='main/about.html',
                  )


def userhomepage(request):
    return render(request = request,
                  template_name='main/categories.html',
                  context = {"categories":TutorialCategory.objects.all})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"New account created:{username}")
            login(request, user)
            messages.info(request,f"You are now logged in as {username}")
            return redirect("main:userhomepage")

        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}: {form.error_messages[msg]}")

    form =NewUserForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def logout_request(request):
  logout(request)
  messages.info(request,"Logged out successfully!!")
  return redirect("main:intro") 

def login_request(request):
  if request.method == "POST":
          form = AuthenticationForm(request,data=request.POST)
          if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user is not None:
              login(request, user)
              messages.info(request,f"You are now logged in as {username}")
              return redirect("main:userhomepage")
            else:
              messages.error(request,"Invalid username or password")  
          else:
            messages.error(request,"Invalid username or password")          



  form=AuthenticationForm()
  return render(request,"main/login.html",{"form":form})


def password_reset(request):
    return render(request=request,template_name='main/password_reset_form.html')



