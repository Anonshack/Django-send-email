import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from send_email import send_email


@csrf_exempt
def send_email(request):
    data = request.POST.get('data', '')
    subject = f'Hello, World! {data}'
    message = str(datetime.datetime.now())
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['anonshack48@gmail.com']
    print('data', data)
    send_mail(subject, message, from_email, recipient_list,
              fail_silently=False)
    return HttpResponse('Email sent successfully!')
