from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Leftovers(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    details = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sold_by = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, null=True,
                                related_name='for_sale_leftovers')
    purchased_by = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, null=True,
                                     related_name='purchased_leftovers')

    def __str__(self):
        return self.title + " (" + self.subtitle + ") for $" + str(self.price)

    def get_absolute_url(self):
        return reverse("leftovers-detail", kwargs={"pk": self.pk})
