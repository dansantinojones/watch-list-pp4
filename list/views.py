from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Media


class MediaList(generic.ListView):
    model = Media
    queryset = Media.objects.filter(status=0).order_by('title')
    template_name = 'index.html'
    paginate_by = 10


class MediaDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Media.objects.filter(status=0)
        media = get_object_or_404(queryset, slug=slug)
        comments = media.comments.filter(approved=True).order_by('created_on')
        recommended = False
        if media.recommended.filter(id=self.request.user.id).exists():
            recommended = True

        return render(
            request,
            "media_detail.html",
            {
                "media": media,
                "comments": comments,
                "recommended": recommended
            },
        )