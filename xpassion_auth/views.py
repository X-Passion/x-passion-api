from django.shortcuts import render
from cas import CASClient

import django_cas_ng.backends
import django.contrib.auth
from django_cas_ng.utils import get_cas_client, get_service_url
from django.core.exceptions import PermissionDenied

import rest_framework_jwt
import warnings

def brcas_token(request):
    service_url = get_service_url(request)
    client = get_cas_client(service_url=service_url, request=request)
    ticket = request.GET.get('ticket')
    if ticket:
        user = django.contrib.auth.authenticate(ticket=ticket, service="https://api.x-passion.binets.fr/api-brcas-token-auth/", request=request)
        if user is not None :
            jwt_payload_handler = rest_framework_jwt.settings.api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = rest_framework_jwt.settings.api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            # TODO : un hard-code redirect_url
            return render(request, "storer.html", context = { "token" : token, "redirect_url" : "https://x-passion.binets.fr/" })
    raise PermissionDenied('BR CAS login failed.')

