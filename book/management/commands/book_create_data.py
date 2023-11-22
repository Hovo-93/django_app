from django.core.management.base import BaseCommand
from book.generate_fate_data_for_book import generate_fake_book_data


class Command(BaseCommand):
    def handle(self, *args, **options):
        generate_fake_book_data(10)
        print('Completed')
