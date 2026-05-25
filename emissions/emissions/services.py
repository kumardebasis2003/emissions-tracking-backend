from decimal import Decimal
import csv
import io
from .models import EmissionRecord

def calculate_emissions(quantity, emission_factor=None):
    """Calculate total emissions in tCO2e"""
    factor = emission_factor or Decimal('0.001')  # Default fallback
    return quantity * factor

def flag_suspicious(record_data):
    """Validation rules for suspicious flag"""
    qty = record_data.get('quantity', 0)
    if qty < 0:
        return True, 'Negative quantity'
    if qty > 100000:
        return True, 'Extremely high quantity'
    if not record_data.get('unit') or record_data['unit'].strip() == '':
        return True, 'Missing unit'
    return False, None

def export_emissions_to_csv(queryset):
    """Generate CSV file from queryset"""
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(['ID', 'Scope', 'Activity', 'Facility', 'Quantity', 'Unit', 'tCO2e', 'Status', 'Flagged'])
    
    for record in queryset:
        writer.writerow([
            record.id, record.scope, record.activity_type, record.facility,
            float(record.quantity), record.unit, float(record.total_emissions),
            record.review_status, record.suspicious_flag
        ])
    
    buffer.seek(0)
    return buffer.getvalue()