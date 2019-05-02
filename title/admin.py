from django.contrib import admin
from .models import Title
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class TitleResource(resources.ModelResource):

    class Meta:
        model = Title
        skip_unchanged = True
        report_skipped = False
        exclude =('id')
        import_id_fields = ['asin', 'title', 'publisher', 'marketingservices', 'batch']

class TitleAdmin(ImportExportModelAdmin):

    resource_class = TitleResource
    list_display = ('id', 'title',)
    

admin.site.register(Title, TitleAdmin)