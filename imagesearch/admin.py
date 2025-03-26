## admin.py (Admin Dashboard Setup)t
from django.contrib import admin
from .models import SearchReport
import csv
from django.http import HttpResponse

class SearchReportAdmin(admin.ModelAdmin):
    list_display = ('image_name', 'match_found', 'timestamp')
    actions = ['export_as_csv', 'delete_selected']
    
    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="search_reports.csv"'
        writer = csv.writer(response)
        writer.writerow(['Image Name', 'Match Found', 'Timestamp'])
        for report in queryset:
            writer.writerow([report.image_name, report.match_found, report.timestamp])
        return response
    
    export_as_csv.short_description = "Export Selected Reports as CSV"
admin.site.register(SearchReport, SearchReportAdmin)
