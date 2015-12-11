from api.serializers import SimpleUserSerializer
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET',])
def get_main(request, *args, **kwargs):
    return render_to_response('website/main.html', None,
                              context_instance=RequestContext(request))


@require_http_methods(['POST'])
def auth_signup(request, *args, **kwargs):
    signup_username = request.POST['username']
    signup_email = request.POST['email']
    signup_password = request.POST['password']
    try:
        signup_user = User.objects.create_user(signup_username, email=signup_email, password=signup_password)
    except IntegrityError:
        return JsonResponse({'detail':'The email address provided is linked to an existing account'},status=500);
    return auth_signin(request, *args, **kwargs)


@require_http_methods(['POST'])
def auth_signin(request, *args, **kwargs):
    if not request.user.is_authenticated():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if not user: return JsonResponse({'title':'Invalid Account','detail':'Provided login credentials do not match any registered account'},status=500);
        if not user.is_active: return JsonResponse({'title':'Account Disabled','detail':'The requested account has been disabled'},status=500);
        django_login(request, user)
    user_serializer = SimpleUserSerializer(request.user, context={'request':request})
    return JsonResponse(user_serializer.data)
