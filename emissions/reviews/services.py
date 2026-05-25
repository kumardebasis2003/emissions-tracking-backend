from django.db import transaction
from emissions.models import EmissionRecord
from audits.models import AuditLog

def _create_audit_log(record, action, old_data, new_data, user, note=''):
    AuditLog.objects.create(
        emission_record=record,
        action=action,
        old_value=old_data,
        new_value=new_data,
        changed_by=user,
        note=note
    )

@transaction.atomic
def approve_record(record_id, user, note=''):
    record = EmissionRecord.objects.select_for_update().get(id=record_id, company=user.company)
    if record.is_locked:
        raise ValueError("Cannot approve locked record.")
        
    _create_audit_log(record, 'approve', {'status': record.review_status}, {'status': 'approved'}, user, note)
    record.review_status = 'approved'
    record.save(update_fields=['review_status', 'updated_at'])
    return record

@transaction.atomic
def reject_record(record_id, user, note=''):
    record = EmissionRecord.objects.select_for_update().get(id=record_id, company=user.company)
    if record.is_locked:
        raise ValueError("Cannot reject locked record.")
        
    _create_audit_log(record, 'reject', {'status': record.review_status}, {'status': 'rejected', 'note': note}, user, note)
    record.review_status = 'rejected'
    record.save(update_fields=['review_status', 'updated_at'])
    return record

@transaction.atomic
def lock_record(record_id, user):
    record = EmissionRecord.objects.select_for_update().get(id=record_id, company=user.company)
    if record.is_locked:
        raise ValueError("Record already locked.")
        
    _create_audit_log(record, 'lock', {'locked': False}, {'locked': True}, user)
    record.is_locked = True
    record.save(update_fields=['is_locked', 'updated_at'])
    return record