# run with: python manage.py shell < scripts/seed.py
from books.models import Category, Book
c=Category.objects.create(name='Fiction', slug='fiction')
Book.objects.create(category=c, title='The Alchemist', author='Paulo Coelho', description='A poetic tale', price=199.00, stock=10, slug='the-alchemist')
Book.objects.create(category=c, title='1984', author='George Orwell', description='Dystopian novel', price=249.00, stock=5, slug='1984')
print("Seeded")
