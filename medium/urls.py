from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

from .views import (
    NoteListView,
    NoteCreateView,
    NoteUpdateView,
    handle_upload
)


urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),

    url(r"ajax/image-upload/$", handle_upload, name="handle_upload"),

    url(r"^notes/$", NoteListView.as_view(), name="notes_list"),
    url(r"^notes/create/$", NoteCreateView.as_view(), name="notes_create"),
    url(r"^notes/(?P<pk>\d+)/update/$", NoteUpdateView.as_view(), name="notes_update"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
