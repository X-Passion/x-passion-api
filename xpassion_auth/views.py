import django.contrib.auth

from django_cas_ng.utils import (
        get_cas_client,
        get_service_url,
        get_redirect_url )
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

import rest_framework_jwt

def brcas_token(request):
    service_url = get_service_url(request)
    redirect_url = get_redirect_url(request)
    client = get_cas_client(service_url=service_url, request=request)
    ticket = request.GET.get('ticket')
    if ticket:
        user = django.contrib.auth.authenticate(ticket=ticket, service="https://api.x-passion.binets.fr/api-brcas-token-auth/", request=request)
        if user is not None :
            jwt_payload_handler = rest_framework_jwt.settings.api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = rest_framework_jwt.settings.api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return render(request, "storer.html", context = {
                "token" : token,
                "redirect_url" : redirect_url
                })
    raise PermissionDenied('BR CAS login failed.')

