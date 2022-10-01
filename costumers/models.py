from django.db import models

# Create your models here.

from django_tenants.models import TenantMixin, DomainMixin


class Client(TenantMixin):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True


class Domain(DomainMixin):
    pass

