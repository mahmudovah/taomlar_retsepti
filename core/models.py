from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    unit_type = (
        ('g', 'gram'),
        ('kg', 'kilogram'),
        ('dona', 'dona'),
        ('ml','millilitr'),
        ('l', 'litr')
    )
    unit = models.CharField(max_length=10, choices=unit_type)
    quantity = models.PositiveIntegerField(default=1)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.quantity} {self.unit}'
      

class Meal(models.Model):
    name=models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    image =models.ImageField(upload_to='meals/')
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    status_ch = (('activ', 'faol'),('inactive','nofaol'))
    status = models.CharField(max_length=10, choices=status_ch)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Taom'
        verbose_name_plural = 'Taomlar'
        ordering = ["-created_at"]