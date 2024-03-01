# from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


def activate_email(activation_link, email_to):
    subject = "Activate your account today!"

    body = f"""
    Hello!

    Your activation link {activation_link}
    """

    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [email_to],
        fail_silently=False,
    )


