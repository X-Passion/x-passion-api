import django_cas_ng.backends
import django_cas_ng.signals

from django.dispatch import receiver
from django.contrib.auth.models import Group

from re import match

class BRCASBackend(django_cas_ng.backends.CASBackend):
    def clean_username(self, username):
        username = super().clean_username(username);
        username += '@frankiz.net'
        return username

def add_to_group_or_create(user, groupname):
    group,_ = Group.objects.get_or_create(name=groupname)
    user.groups.add(group)

@receiver(django_cas_ng.signals.cas_user_authenticated)
def set_groups(sender, **kwargs):
    if kwargs['created'] :
        brgroups = kwargs['attributes'].get('brMemberOf') or []
        promo = kwargs['attributes'].get('brPromo')
        if ('formation_x' in brgroups) and match(r'[0-9]{4}', promo):
                add_to_group_or_create(kwargs['user'], 'polytechnique_ingenieur_'+promo)



