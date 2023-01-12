from django.shortcuts import render
from django.views import generic


class MediaList(generic.ListView):
    model = Media
    queryset = Media.objects.filter(status=0).order_by('title')
    template_name = 'index.html'
    paginate_by = 10