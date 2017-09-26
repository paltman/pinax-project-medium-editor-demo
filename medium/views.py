from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, UpdateView, ListView

from account.decorators import login_required
from account.mixins import LoginRequiredMixin
from pinax.images.models import ImageSet

from .models import Note


class NoteListView(ListView):
    model = Note

    def get_queryset(self, *args, **kwargs):
        return self.request.user.note_set.all()


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = [
        "title",
        "content"
    ]

    def form_valid(self, form):
        note = form.save(commit=False)
        note.author = self.request.user
        note.save()
        return redirect("notes_list")


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = [
        "title",
        "content"
    ]

    def get_queryset(self, *args, **kwargs):
        return self.request.user.note_set.all()

    def get_success_url(self):
        return reverse("notes_list")


@login_required
@require_POST
def handle_upload(request):
    image_set, _ = ImageSet.objects.get_or_create(created_by=request.user)
    data = {"files": []}
    for file in request.FILES.getlist("files[]"):
        image = image_set.images.create(image=file, original_filename=file.name, created_by=request.user)
        data["files"].append({
            "url": image.image.url  # @@@ will want to use right size thumbnail / http://api.jquery.com/jQuery.ajax/ - converters might be a clue here
        })
    return JsonResponse(data)
