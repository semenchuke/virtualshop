from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
import django.contrib.auth as auth
from django.urls import reverse


def login(request):
    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST or None)
        username = request.POST.get('username')
        password = request.POST['password']
        # print(f'пришла заполненная форма: {username}, {password}')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('index'))

    else:
        form = ShopUserLoginForm()


    content = {
        'form': form,
        'title': 'Log in',
        'next': next,
    }

    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def registr(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {
        'title': 'registration',
        'form': register_form
    }

    return render(request, 'authapp/registr.html', content)

def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        register_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {
        'title': 'edit',
        'form': edit_form
    }

    return render(request, 'authapp/edit.html', content)
