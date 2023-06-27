from django.core.management.base import BaseCommand
import pandas as pd
from myapp.models import Voucher

class Command(BaseCommand):
    help = 'Exports data from Django models to a flat file'

    def handle(self, *args, **options):
        queryset = Voucher.objects.all()  # Replace 'YourModel' with your actual model name

        # Convert queryset to a pandas DataFrame
        df = pd.DataFrame(list(queryset.values()))

        # Export DataFrame to a flat file
        file_path = 'vouchers.csv'  # Specify the path where you want to save the file
        df.to_csv(file_path, index=False)  # You can use different file formats and options here
        self.stdout.write(self.style.SUCCESS(f'Data exported successfully to {file_path}'))