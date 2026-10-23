from django.core.management.base import BaseCommand
from apps.models import Category, Product

DATA = {
    "Telefonlar": [
        ("iPhone 15", "Apple smartfoni, 128 GB", 999),
        ("Samsung Galaxy S24", "Android flagman, 256 GB", 899),
        ("Xiaomi 14", "Tez va arzon flagman", 699),
    ],
    "Noutbuklar": [
        ("MacBook Air M3", "Yengil va tez noutbuk", 1299),
        ("Lenovo ThinkPad", "Ish uchun ishonchli noutbuk", 1099),
        ("Asus ROG", "O'yinlar uchun kuchli noutbuk", 1599),
    ],
    "Quloqchinlar": [
        ("AirPods Pro", "Shovqinni yutuvchi quloqchin", 249),
        ("Sony WH-1000XM5", "Simsiz katta quloqchin", 349),
    ],
}


class Command(BaseCommand):
    help = "Test kategoriya va mahsulotlarni yaratadi"

    def handle(self, *args, **options):
        for cat_name, items in DATA.items():
            cat, _ = Category.objects.get_or_create(
                name=cat_name, defaults={"description": f"{cat_name} bo'limi"}
            )
            for name, desc, price in items:
                Product.objects.get_or_create(
                    name=name,
                    defaults={"category": cat, "short_description": desc, "price": price},
                )
        self.stdout.write(self.style.SUCCESS("Tayyor: kategoriya va mahsulotlar yaratildi"))
