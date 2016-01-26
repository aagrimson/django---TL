import os
import csv
from django.conf import settings
from tl.models import Store
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        print "Loading CSV"
        csv_path = os.path.join(settings.BASE_DIR, "store_file.csv")
        csv_file = open(csv_path, 'rb')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
        	obj = Store.objects.create(
                test_no=row['test_no'],
                location_id=row['location_id'],
                test_store=row['test_store'],
                pair=row['pair']
            )
