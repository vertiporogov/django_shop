from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        product_list = [
            {'name': 'phone', 'price': 50000, 'category': 1},
            {'name': 'tv', 'price': 100000, 'category': 1},
        ]

        product_for_creats = []
        for product_item in product_list:
            product_for_creats.append(Product(**product_item))

        Product.objects.bulk_create(product_for_creats)
