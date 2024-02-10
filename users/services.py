from django.conf import settings
from django.core.mail import send_mail


def send_new_password(email, new_password):
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль : {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )


def send_registration(email, token):
    send_mail(
        subject='Подтверждение почты',
        message=f'Для завершения регистрации перейдите по ссылке  http://127.0.0.1:8000/users/validate/{token}/',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
