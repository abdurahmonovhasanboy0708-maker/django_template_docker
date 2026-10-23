from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField("Nomi", max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField("Tavsif", blank=True)
    image = models.ImageField("Rasm", upload_to="categories/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField("Nomi", max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField("Qisqa tavsif", max_length=255)
    price = models.DecimalField("Narx", max_digits=10, decimal_places=2)
    image = models.ImageField("Rasm", upload_to="products/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name