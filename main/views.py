from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserForm, RegistrationForm
from django.http import JsonResponse
from django.contrib.auth.models import User

# Регистрация нового пользователя
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Войти сразу после регистрации
            return redirect('user_list')
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})

# Список пользователей (поиск + защита)
@login_required
def user_list(request):
    query = request.GET.get('q', '')
    if query:
        users = User.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))
    else:
        users = User.objects.all()
    return render(request, 'main/user_list.html', {'users': users, 'query': query})

# Форма добавления/редактирования
@login_required
def user_form(request, id=None):
    user = get_object_or_404(User, pk=id) if id else None
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'main/user_form.html', {'form': form})

# Удаление пользователя
@login_required
def user_delete(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    return redirect('user_list')

def user_list_api(request):
    users = User.objects.all().values('id', 'username', 'email')
    return JsonResponse(list(users), safe=False)