from django.contrib import admin
from .models import keyword
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class keywordResource(resources.ModelResource):

    class Meta:
        model = keyword
        skip_unchanged = True
        report_skipped = False
        exclude =('id')
        import_id_fields = ['keyword']

class KeywordAdmin(ImportExportModelAdmin):

    resource_class = keywordResource
    list_display = ('id', 'keyword',)
    

admin.site.register(keyword, KeywordAdmin)