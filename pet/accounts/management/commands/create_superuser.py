from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a default superuser if it does not exist'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                password="it'sadminpassword123",
                email="admin@admin.com"
            )
            self.stdout.write(self.style.SUCCESS('Default superuser created'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
