from django.db.models import Sum

from emissions.models import EmissionRecord


def get_dashboard_stats(company):

    qs = EmissionRecord.objects.filter(
        company=company
    )

    total_emissions = qs.aggregate(
        total=Sum('total_emissions')
    )['total'] or 0

    return {

        'total_records':
            qs.count(),

        'approved':
            qs.filter(
                review_status='approved'
            ).count(),

        'pending':
            qs.filter(
                review_status='pending'
            ).count(),

        'rejected':
            qs.filter(
                review_status='rejected'
            ).count(),

        'suspicious':
            qs.filter(
                suspicious_flag=True
            ).count(),

        'total_emissions':
            float(total_emissions),

        'by_scope': {

            'Scope 1':
                qs.filter(
                    scope='Scope 1'
                ).count(),

            'Scope 2':
                qs.filter(
                    scope='Scope 2'
                ).count(),

            'Scope 3':
                qs.filter(
                    scope='Scope 3'
                ).count(),
        },

        # Simple source grouping
        'by_source': {

            'Fuel':
                qs.filter(
                    activity_type__icontains='Fuel'
                ).count(),

            'Electricity':
                qs.filter(
                    activity_type__icontains='Electricity'
                ).count(),

            'Travel':
                qs.filter(
                    activity_type__icontains='Travel'
                ).count(),
        }
    }