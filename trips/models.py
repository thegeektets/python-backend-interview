from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Trip(models.Model):
    driver_id = models.IntegerField()
    vehicle_id = models.IntegerField()
    customer_id = models.IntegerField()
    address = models.CharField(max_length=50, null=True)
    cargo_tonnage = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    address_type = models.TextChoices('pickup_point', 'drop_off_point')
    done_by_user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING),
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s , %s , %s" % (self.id, self.customer_id, self.address)
