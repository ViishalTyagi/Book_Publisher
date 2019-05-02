from django.shortcuts import render, redirect
from django.views.generic import ListView
from book.models import books
from keywords.models import keyword

def home(request):
    context = {
        "content": "Search your favorite books here!"
    }
    return render(request, "home.html", context)

class view_all(ListView):
    template_name = "view_all.html"

    def get_context_data(self, *args, **kwargs):
        context = super(view_all ,self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None and len(query)>0 and keyword.objects.search(query):
            return books.objects.search_all(query).order_by('-date')         
        query = None
        return None

class view_orim(ListView):
    template_name = "view_all.html"

    def get_context_data(self, *args, **kwargs):
        context = super(view_orim ,self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        context['publisher'] = self.request.GET.get('p')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q', None)
        publisher = request.GET.get('p', None)
        if query is not None and len(query)>0 and keyword.objects.search(query):
            if query is not None and publisher is not None:
                if len(query)>0 and len(publisher)>0:
                    return books.objects.orim(query, publisher).order_by('-date')

                return books.objects.search_all(query).order_by('-date')

            elif query is not None and publisher is None:
                return books.objects.search_all(query).order_by('-date')

            return books.objects.featured(query).order_by('-date')

        elif len(query)==0 and len(publisher)>0:
            return books.objects.featured('Open Road Media').order_by('-date')

        return None
        




        


