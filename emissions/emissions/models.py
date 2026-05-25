from django.db import models

class EmissionRecord(models.Model):
    STATUS = [('pending','Pending'),('approved','Approved'),('rejected','Rejected')]
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    scope = models.CharField(max_length=20)
    activity_type = models.CharField(max_length=100)
    facility = models.CharField(max_length=255, blank=True)
    quantity = models.DecimalField(max_digits=15, decimal_places=4)
    unit = models.CharField(max_length=20)
    total_emissions = models.DecimalField(max_digits=15, decimal_places=4)
    review_status = models.CharField(max_length=10, choices=STATUS, default='pending')
    suspicious_flag = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta: db_table = 'emission_record'
    def __str__(self): return f"{self.id} - {self.activity_type}"