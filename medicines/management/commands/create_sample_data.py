from django.core.management.base import BaseCommand
from medicines.models import Medicine
from datetime import date, timedelta
from decimal import Decimal


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
                'name': 'PARACETAMOL-650',
                'description': 'Paracetamol is a common painkiller used to treat aches and pain. It can also be used to reduce a high temperature.',
                'batch_number': 'DOBS3797',
                'manufacturing_date': date(2025, 2, 21),
                'expiry_date': date(2028, 2, 21),
                'manufacturer': 'MediHealth Pharmaceuticals',
                'mrp': Decimal('33.76'),
                'caution': 'CAUTION: Taking paracetamol daily dose may cause serious liver damage or allergic reactions.'
            },
            {
                'name': 'ASPIRIN-75',
                'description': 'Aspirin is used to reduce fever and relieve mild to moderate pain from conditions such as headaches, toothaches, and muscle aches.',
                'batch_number': 'ASP2024001',
                'manufacturing_date': date.today() - timedelta(days=60),
                'expiry_date': date.today() + timedelta(days=300),
                'manufacturer': 'PharmaCorp Ltd',
                'mrp': Decimal('45.20'),
                'caution': 'Do not exceed recommended dosage. Consult your doctor if symptoms persist.'
            },
            {
                'name': 'IBUPROFEN-400',
                'description': 'Ibuprofen is a nonsteroidal anti-inflammatory drug (NSAID) used to treat pain, fever, and inflammation.',
                'batch_number': 'IBU003',
                'manufacturing_date': date.today() - timedelta(days=30),
                'expiry_date': date.today() + timedelta(days=500),
                'manufacturer': 'HealthCare Inc',
                'mrp': Decimal('28.90'),
                'caution': 'May cause stomach irritation. Take with food. Not suitable for children under 12.'
            },
            {
                'name': 'AMOXICILLIN-500',
                'description': 'Amoxicillin is an antibiotic used to treat bacterial infections including respiratory tract infections.',
                'batch_number': 'AMX2024',
                'manufacturing_date': date.today() - timedelta(days=15),
                'expiry_date': date.today() + timedelta(days=365),
                'manufacturer': 'AntiBio Pharma',
                'mrp': Decimal('120.50'),
                'caution': 'Complete the full course as prescribed. Do not skip doses. May cause drowsiness.'
            },
            {
                'name': 'VITAMIN C-500',
                'description': 'Vitamin C supplement to boost immunity and support overall health.',
                'batch_number': 'VIT005',
                'manufacturing_date': date.today() - timedelta(days=20),
                'expiry_date': date.today() + timedelta(days=600),
                'manufacturer': 'VitaLife Supplements',
                'mrp': Decimal('85.00'),
                'caution': 'Store in a cool, dry place. Keep away from children.'
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
