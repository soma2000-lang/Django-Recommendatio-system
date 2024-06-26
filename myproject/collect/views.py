from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from collector.models import Log
import datetime

from django.views.decorators.csrf import ensure_csrf_cookie
# Ensure_csrf_cookie appears to be a decorator commonly used in web development frameworks, such as Django in Python. This decorator is typically used to ensure that a Cross-Site Request Forgery (CSRF) cookie is set when rendering a response.
    if request.method == 'POST':
        date = request.GET.get('date', datetime.datetime.now())

        user_id = request.POST['user_id']
        content_id = request.POST['content_id']
        event = request.POST['event_type']
        session_id = request.POST['session_id']
        l = Log(
            created=date,
            user_id=user_id,
            content_id=str(content_id),
            event=event,
            session_id=str(session_id))
        l.save()
    else:
        HttpResponse('log only works with POST')
    return HttpResponse('ok')