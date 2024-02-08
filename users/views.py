import random
from uuid import uuid4

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.is_active = False
        new_user.token = self.token_generate()
        new_user.save()

        send_mail(
            subject='Подтверждение почты',
            message=f'Для завершения регистрации перейдите по ссылке  http://127.0.0.1:8000/users/validate/{new_user.token}/',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )

        return redirect(reverse('catalog:home'))

    def token_generate(self):
        return str(uuid4())


def confirm_email(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.token = None
    user.save()
    return redirect(reverse('catalog:home'))


class UserProfileView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = User.objects.make_random_password()
    email = request.POST['email']
    user = get_object_or_404(User, email=email)
    # print(email)
    user.set_password(new_password)
    user.save()
    send_mail(
        subject='Восстановление пароля',
        message=f'Ваш новый пароль {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email]
    )
    return redirect(reverse('catalog:home'))
