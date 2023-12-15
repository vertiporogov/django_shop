from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        product_dict = {'pk': 1, 'name': 'phone', 'price': 50000, 'category': 1}

        Product.objects.bulk_create(product_dict)
