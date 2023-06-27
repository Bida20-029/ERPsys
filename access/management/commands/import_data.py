from django.core.management.base import BaseCommand
from access.models import Payment
import pandas as pd

class Command(BaseCommand):
    help = 'Import data from Excel file to model'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help=r'C:\Users\offic\Desktop\ERPsys\payment.xlsx')

    def handle(self, *args, **options):
        file_path = options['file_path']
        df = pd.read_excel(file_path)

        for _, row in df.iterrows():
            your_model_instance = Payment(
                Voucher_ID=row['VoucherID'],
                PVNumber=row['PVNumber'],
                Paid_To=row['PaidTo'],
                Prepared_By=row['PreparedBy'],
                Funds_use_breakdown=row['FundsUseBreakdown'],
                Amount_in_words=row['AmountInWords'],
                Amount=row['Amount'],
                Date=row['Date_']
                # Map other columns accordingly
            )
            your_model_instance.save()
