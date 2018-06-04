from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from myplakaApp.models import Search as Car, Search

from .forms import SaveForm, LoginForm, RegisterForm


def home(request):
    return render(request, 'homepage1.html', {})


def form_view(request):
    return render(request, 'form.html', locals())


def search_view(request):
    if 'i' in request.GET and request.GET['i']:
        i = request.GET['i']
        arac = Car.objects.filter(plaka__icontains=i)
        return render(request, 'show.html', {'cars': arac, 'query': i})
    else:
        HttpResponse('Search')

def create_plaka(request):
    form=SaveForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        'title':'Register',
    }

    return render(request,'form2.html',context)

""" def bildirim_view(request):
    post = get_object_or_404(Search)

    form = BildirimForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'post': post,
        'form': form
    }
    return render(request, "show.html", context)
"""

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        return render(request,'homepage1.html')

    context = {
        'form': form,
        'title':'Giris Yap'
    }
    return render(request, 'girisform.html', context)

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        # user.is_staff = user.is_superuser = True
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return render(request, 'homepage1.html')

    return render(request, "form2.html", {"form": form, 'title': 'Uye Ol'})

def logout_view(request):
    logout(request)
    return render(request, 'homepage1.html')