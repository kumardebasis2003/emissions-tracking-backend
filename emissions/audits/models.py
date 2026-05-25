from django.db import models
from django.conf import settings

class AuditLog(models.Model):
    emission_record = models.ForeignKey('emissions.EmissionRecord', on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    old_value = models.JSONField(null=True, blank=True)
    new_value = models.JSONField(null=True, blank=True)
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    changed_at = models.DateTimeField(auto_now_add=True)
    class Meta: db_table = 'audit_log'