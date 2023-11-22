import os

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_notification(email):
    """Отправка уведомления при регистрации """
    subject = 'Welcome!'
    message = 'Thank you for registering!'
    from_email = os.getenv('FROM_EMAIL')
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    return 'Done'

