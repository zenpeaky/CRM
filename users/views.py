# views
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.http import JsonResponse

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://localhost:8000/api/v1/auth/google/login/callback/'
    client_class = OAuth2Client

def google_callback(request):
    code, scope = str(request.GET['code']), str(request.GET['scope'])
    json_obj = {'code': code, 'scope': scope}

    return JsonResponse(json_obj)