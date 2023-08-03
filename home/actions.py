import csv
from django.http import HttpResponse

def export_selected_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="selected_records.csv"'
    writer = csv.writer(response)
    writer.writerow([field.name for field in queryset.model._meta.fields])
    for obj in queryset:
        writer.writerow([getattr(obj, field.name) for field in queryset.model._meta.fields])
    return response
export_selected_as_csv.short_description = "Export selected as CSV"
