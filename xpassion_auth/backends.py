import django_cas_ng.backends

class BRCASBackend(django_cas_ng.backends.CASBackend):
    def clean_username(self, username):
        username = super().clean_username(username);
        username += '@frankiz.net'
        return username
