from django.core.management.base import BaseCommand
from medicines.models import Medicine


class Command(BaseCommand):
    help = 'Clear all medicines from the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force deletion without confirmation',
        )

    def handle(self, *args, **options):
        count = Medicine.objects.count()
        
        if count == 0:
            self.stdout.write(
                self.style.WARNING('No medicines found in the database.')
            )
            return
        
        if not options['force']:
            confirm = input(f'Are you sure you want to delete all {count} medicines? Type "yes" to confirm: ')
            if confirm.lower() != 'yes':
                self.stdout.write(
                    self.style.WARNING('Operation cancelled.')
                )
                return
        
        Medicine.objects.all().delete()
        self.stdout.write(
            self.style.SUCCESS(f'Successfully deleted {count} medicines!')
        )
