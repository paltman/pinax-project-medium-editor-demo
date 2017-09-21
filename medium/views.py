from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, ListView

from account.mixins import LoginRequiredMixin

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
