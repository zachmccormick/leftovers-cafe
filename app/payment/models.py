from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Purchase(models.Model):
    leftover = models.OneToOneField(to='inventory.Leftovers', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.leftover.title + " (purchased by" + self.user.name + ")"

    def get_absolute_url(self):
        return reverse("purchase-detail", kwargs={"pk": self.pk})
