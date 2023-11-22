from faker import Faker
from book.models import Book

fake = Faker(['ru_RU'])


def generate_fake_book_data(count):
    for _ in range(count):
        books = Book.objects.create(
            title=fake.catch_phrase(),
            author=fake.name(),
            year=fake.random_int(min=1800, max=2023),
            isbn=fake.isbn13()
        )
        books.save()