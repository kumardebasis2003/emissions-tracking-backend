from django.db import transaction
from django.utils import timezone
from decimal import Decimal
from companies.models import Company
from emissions.models import EmissionRecord
from .models import DataSource, RawRecord
import pandas as pd

@transaction.atomic
def process_sap_upload(company_id, dataframe, user):
    company = Company.objects.get(id=company_id)
    source = DataSource.objects.create(company=company, source_type='SAP', uploaded_by=user, record_count=len(dataframe))
    
    created_count = 0
    errors = []
    
    for idx, row in dataframe.iterrows():
        try:
            qty = Decimal(str(row['Qty']))
            unit = str(row['Unit']).strip().upper()
            
            # Normalize GAL to Liters
            if unit == 'GAL':
                qty = qty * Decimal('3.78541')
                unit = 'L'
            
            # Default emission factor for fuel
            factor = Decimal('0.00268') if unit == 'L' else Decimal('0.00232')
            total = qty * factor
            
            EmissionRecord.objects.create(
                company=company,
                source_record=None,  # Link later if needed
                scope='Scope 1',
                category=str(row['Fuel Type']),
                activity_type='Stationary Combustion',
                facility=str(row.get('Plant Code', 'Unknown')),
                quantity=qty,
                unit=unit,
                normalized_quantity=qty,
                normalized_unit=unit,
                emission_factor=factor,
                total_emissions=total,
                review_status='pending'
            )
            created_count += 1
        except Exception as e:
            errors.append(f"Row {idx}: {str(e)}")
            
    source.record_count = created_count
    source.save()
    return {'source_id': source.id, 'records_count': created_count, 'errors': errors}

@transaction.atomic
def process_utility_upload(company_id, dataframe, utility_type, user):
    company = Company.objects.get(id=company_id)
    source = DataSource.objects.create(company=company, source_type='UTILITY', uploaded_by=user, record_count=len(dataframe))
    
    created_count = 0
    for idx, row in dataframe.iterrows():
        kwh = Decimal(str(row['kWh']))
        factor = Decimal('0.000366')  # Default grid factor
        total = kwh * factor
        
        EmissionRecord.objects.create(
            company=company,
            scope='Scope 2',
            category='Purchased Electricity',
            activity_type='Grid Electricity',
            facility=str(row.get('site_code', 'Unknown')),
            quantity=kwh,
            unit='kWh',
            normalized_quantity=kwh,
            normalized_unit='kWh',
            emission_factor=factor,
            total_emissions=total,
            review_status='pending'
        )
        created_count += 1
        
    source.record_count = created_count
    source.save()
    return {'source_id': source.id, 'records_count': created_count}

@transaction.atomic
def process_travel_upload(company_id, data, user):
    company = Company.objects.get(id=company_id)
    source = DataSource.objects.create(company=company, source_type='TRAVEL', uploaded_by=user, record_count=1)
    
    distance = Decimal(str(data['distance_km']))
    factor = Decimal('0.0002')  # Default travel factor
    total = distance * factor
    
    record = EmissionRecord.objects.create(
        company=company,
        scope='Scope 3',
        category='Business Travel',
        activity_type=data['travel_type'],
        facility=f"{data['from_location']} -> {data['to_location']}",
        quantity=distance,
        unit='km',
        normalized_quantity=distance,
        normalized_unit='km',
        emission_factor=factor,
        total_emissions=total,
        review_status='pending'
    )
    return {'emission_id': record.id, 'total_emissions': total}