from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse

from mainapp.models import ProductCategory
from authapp.models import ShopUser
from adminapp.forms import ShopUserCreateForm, ShopUserUpdateForm, ProductCategoryUpdateForm


@user_passes_test(lambda user: user.is_superuser)
def main(request):
    title = 'администрирование'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', \
                                                 'username')

    context = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', context)


def user_create(request):
    title = 'новый пользователь'
    value = 'создать пользователя'

    if request.method == 'POST':
        form = ShopUserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:main'))
    else:
        form = ShopUserCreateForm()


    context = {
        'title': title,
        'form': form,
        'value': value,
    }

    return render(request, 'adminapp/user_update.html', context)


def user_update(request, pk):
    title = 'редактирование пользователя'
    value = 'обновить данные'

    user_to_update = get_object_or_404(ShopUser, pk=int(pk))

    if request.method == 'POST':
        form = ShopUserUpdateForm(request.POST, request.FILES, instance=user_to_update)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:main'))
    else:
        form = ShopUserUpdateForm(instance=user_to_update)

    context = {
        'title': title,
        'form': form,
        'value': value,
    }

    return render(request, 'adminapp/user_update.html', context)


def user_delete(request, pk):
    title = 'удаление пользователя'
    user_to_del = get_object_or_404(ShopUser, pk=int(pk))

    if request.method == 'POST':
        user_to_del.is_active = False
        user_to_del.save()
        return HttpResponseRedirect(reverse('adminapp:main'))
    else:
        context = {
            'title': title,
            'user_to_delete': user_to_del,
        }

        return render(request, 'adminapp/user_delete.html', context)


def categories(request):
    title = 'администрирование/категории'

    objects_list = ProductCategory.objects.all().order_by('name')

    context = {
        'title': title,
        'objects': objects_list,
    }

    return render(request, 'adminapp/categories.html', context)


def category_create(request):
    title = 'новая категория'
    value = 'создать категорию'

    if request.method == 'POST':
        form = ProductCategoryUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        form = ProductCategoryUpdateForm()


    context = {
        'title': title,
        'form': form,
        'value': value,
    }

    return render(request, 'adminapp/category_update.html', context)


def category_update(request, pk):
    title = 'изменить категорию'

    category_to_update = get_object_or_404(ProductCategory, pk=int(pk))

    if request.method == 'POST':
        form = ProductCategoryUpdateForm(request.POST, request.FILES, instance=category_to_update)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        form = ProductCategoryUpdateForm(instance=category_to_update)


    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'adminapp/category_update.html', context)


def category_delete(request, pk):
    title = 'удаление категории'
    category_to_del = get_object_or_404(ProductCategory, pk=int(pk))

    if request.method == 'POST':
        category_to_del.is_active = False
        category_to_del.save()
        return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        context = {
            'title': title,
            'category_to_delete': category_to_del,
        }

        return render(request, 'adminapp/category_delete.html', context)