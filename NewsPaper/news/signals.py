from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostCategory




def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/NewsPaper/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'create_news':
        categories = instance.category.all()
        subscribers_email = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_email += [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers_email)


def send_welcome_email(user):
    subject = 'Добро пожаловать на наш сайт!'
    message = render_to_string('accounts/email/welcome_email.html', {'user': user})
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email]
    )
    email.content_subtype = 'html'
    email.send()


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        send_welcome_email(instance)