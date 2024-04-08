from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import User, Teacher

# Create your views here.

def UserLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'login_page.html',{})

    return render(request, 'login_page.html',{})


def UserLogout(request):
    auth.logout(request)
    return redirect('/')


def AddNewTeacher(request):
    no_role_user_set = User.objects.filter(parents__isnull=True, teacher__isnull=True)
    if request.method == "POST":
        user = User.objects.get(pk=request.POST.get('abstract_user'))
        user.nickname = request.POST.get('nickname')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.th_first_name = request.POST.get('th_first_name')
        user.th_last_name = request.POST.get('th_last_name')
        user.email = request.POST.get('email')
        user.birth_date = request.POST.get('birth_date')
        user.save()

        teacher = Teacher()
        teacher.abstract_user = user
        teacher.id_card_number = request.POST.get('id_card_number')
        teacher.info = request.POST.get('info')
        teacher.save()
        return render(request, 'landing-page.html',{})
    print(no_role_user_set)
    return render(request, 'add_new_teacher.html',{"user_set":no_role_user_set})