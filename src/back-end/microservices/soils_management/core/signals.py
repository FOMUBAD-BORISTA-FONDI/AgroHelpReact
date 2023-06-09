from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Soil

from .serializers import _SoilSerializer


@receiver(post_save, sender=Soil)
def notify_culture_service(sender, instance, created, **kwargs):
    from .producer import publish

    data = _SoilSerializer(instance)
    if created:
        publish("soil_created", data.data)
