import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_for_creats = []
        product_for_creats = []

        with open('data.json', encoding='utf-16') as file:
            data = json.load(file)
            for i in data:
                if i['model'] == 'catalog.category':
                    category_for_creats.append(i['fields'])
                elif i['model'] == 'catalog.product':
                    product_for_creats.append(i['fields'])

