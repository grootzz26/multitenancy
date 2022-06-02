from django.db import models


# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=50)
    subdomain = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

class members(TenantAwareModel):
    member = models.CharField(max_length=50)


