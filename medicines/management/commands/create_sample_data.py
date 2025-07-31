from django.core.management.base import BaseCommand
from medicines.models import Medicine
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Create sample medicine data for testing'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing medicines before creating new ones',
        )

    def handle(self, *args, **options):
        if options['clear']:
            # Clear existing data
            count = Medicine.objects.count()
            Medicine.objects.all().delete()
            self.stdout.write(
                self.style.WARNING(f'Cleared {count} existing medicines.')
            )
        
        # Create sample medicines
        sample_medicines = [
            {
                'name': 'Aspirin',
                'batch_number': 'ASP001',
                'manufacturing_date': date.today() - timedelta(days=60),
                'expiry_date': date.today() + timedelta(days=300),
                'manufacturer': 'PharmaCorp'
            },
            {
                'name': 'Paracetamol',
                'batch_number': 'PAR002',
                'manufacturing_date': date.today() - timedelta(days=45),
                'expiry_date': date.today() + timedelta(days=400),
                'manufacturer': 'MediHealth'
            },
            {
                'name': 'Ibuprofen',
                'batch_number': 'IBU003',
                'manufacturing_date': date.today() - timedelta(days=30),
                'expiry_date': date.today() + timedelta(days=500),
                'manufacturer': 'HealthCare Inc'
            },
            {
                'name': 'Expired Medicine',
                'batch_number': 'EXP004',
                'manufacturing_date': date.today() - timedelta(days=800),
                'expiry_date': date.today() - timedelta(days=10),  # Expired
                'manufacturer': 'OldPharma'
            },
            {
                'name': 'Vitamin C',
                'batch_number': 'VIT005',
                'manufacturing_date': date.today() - timedelta(days=20),
                'expiry_date': date.today() + timedelta(days=600),
                'manufacturer': 'VitaLife'
            }
        ]
        
        for medicine_data in sample_medicines:
            medicine = Medicine.objects.create(**medicine_data)
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created medicine: {medicine.name} - {medicine.batch_number}'
                )
            )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {len(sample_medicines)} sample medicines!'
            )
        )
