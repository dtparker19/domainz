from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from domainz import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index_view, name="index"),
    path("", include("domainz.auth.urls")),
    path("", include("domainz.billing.urls")),
]

if settings.DEBUG is True:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        path("__reload__/", include("django_browser_reload.urls")),
    ]
