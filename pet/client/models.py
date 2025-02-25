from django.db import models

# Modelo para dueños
class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    class Meta:
        unique_together = ('first_name', 'last_name')  # Restricción única

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Modelo para mascotas
class Pet(models.Model):
    CATEGORY_CHOICES = [
        ('cat', 'Gato'),
        ('dog', 'Perro'),
        ('bird', 'Ave'),
        ('fish', 'Pez'),
        ('aquatic', 'Animal Acuático'),
        ('other', 'Otro (Insecto/Reptil)'),
    ]

    GRAVITY_CHOICES = [
        ('low', 'No Grave'),
        ('high', 'Grave'),
    ]

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='pet_images/', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Macho'), ('female', 'Hembra')])
    birth_date = models.DateField(null=True, blank=True)
    breed = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    illness = models.CharField(max_length=100)
    illness_gravity = models.CharField(max_length=10, choices=GRAVITY_CHOICES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='pets')

    def __str__(self):
        return f"{self.name} ({self.category})"
