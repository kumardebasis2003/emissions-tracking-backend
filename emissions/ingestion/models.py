from django.db import models
from django.conf import settings

class DataSource(models.Model):
    TYPES = [('SAP','SAP'),('UTILITY','Utility'),('TRAVEL','Travel')]
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    source_type = models.CharField(max_length=10, choices=TYPES)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    class Meta: db_table = 'data_source'