from django.db import models

class TrackingModel(models.model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Ordering
    class Meta:
        abstract = True
        ordering = ('-created_at',)