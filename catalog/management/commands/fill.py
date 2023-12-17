import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_for_creats = []
        product_for_creats = []

        with open('data.json', encoding='utf-8') as file:
            data = json.load(file)
            for i in data:
                if i['model'] == 'catalog.category':
                    category_for_creats.append(i['fields'])
                elif i['model'] == 'catalog.product':
                    product_for_creats.append(i['fields'])

        # product_list = [
        #     {'pk': 1, 'name': 'phone', 'price': 50000, 'category_id': 1},
        #     {'pk': 2, 'name': 'tv', 'price': 100000, 'category_id': 1},
        # ]

        # product_for_creats = []
        # for product_item in product_list:
        #     product_for_creats.append(Product(**product_item))
        #
        # Product.objects.bulk_create(product_for_creats)
