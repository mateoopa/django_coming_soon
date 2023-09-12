from django.core.management.base import BaseCommand
from apps.home.models import Section, Content
from django.contrib.auth.models import User
from core.settings import DEFAULT_USER, DEFAULT_USER_PW


class Command(BaseCommand):
    help = 'Create default sections and user.'

    def handle(self, *args, **kwargs):
        user = User.objects.create_user(username=DEFAULT_USER, password=DEFAULT_USER_PW,
                                        is_staff=True, is_superuser=True)
        section = Section.objects.create(name='Home', created_by_id=user.id, description='Default Section')
        Content.objects.create(created_by_id=user.id, section=section, tittle='Welcome!',
                               description="We're working hard to finish the development of this site. Sign up below to"
                                           "receive updates and to be notified when we launch!")

        self.stdout.write("Default objects created successfully")
