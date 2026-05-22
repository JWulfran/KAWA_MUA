from django.db import models

# Create your models here.
class Service(models.Model):
    CATEGORY_CHOICES = [
        ("makeup", "Maquillage"),
        ("hair", "Coiffure"),
        ("package", "Forfait"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Durée en minutes")
    image = models.ImageField(upload_to="services/", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["category", "name"]

    def __str__(self):
        return self.name