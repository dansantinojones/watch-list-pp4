from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import Media
from .forms import CommentForm


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
                "commented": False,
                "recommended": recommended,
                "comment_form": CommentForm()
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Media.objects.filter(status=0)
        media = get_object_or_404(queryset, slug=slug)
        comments = media.comments.filter(approved=True).order_by('created_on')
        recommended = False
        if media.recommended.filter(id=self.request.user.id).exists():
            recommended = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.media = media
            comment.save()

        else:
            comment_form = CommentForm()

        return render(
            request,
            "media_detail.html",
            {
                "media": media,
                "comments": comments,
                "commented": True,
                "recommended": recommended,
                "comment_form": CommentForm()
            },
        )


class MediaRecommended(View):

    def post(self, request, slug):
        media = get_object_or_404(Media, slug=slug)

        if media.recommended.filter(id=request.user.id).exists():
            media.recommended.remove(request.user)
        else:
            media.recommended.add(request.user)
            
        return HttpResponseRedirect(reverse('media_detail', args=[slug]))


class AddMedia(CreateView):

    model = Media
    fields = ['title', 'description', 'platform', 'genre', 'type', 'media_image']
