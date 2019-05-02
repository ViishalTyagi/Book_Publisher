from django.contrib import admin
from .models import books
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class booksResource(resources.ModelResource):

    class Meta:
        model = books
        skip_unchanged = True
        report_skipped = False
        exclude =('id')
        import_id_fields = ['title', 'author', 'page', 'position', 'sales_rank', 'publisher', 'asin', 'keyword', 'pages']
        # import_id_fields = ('title', 'keyword')

class BookAdmin(ImportExportModelAdmin):

    resource_class = booksResource
    # list_display = ('title', 'publisher', 'author', 'page', 'position')
    

admin.site.register(books, BookAdmin)