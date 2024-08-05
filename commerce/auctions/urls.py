from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listing/<str:title>", views.listing, name="listing"),
    path("edit_watchlist/<str:action>/<str:id>", views.edit_watchlist, name="edit_watchlist"),
    path("watchlist", views.watchlist, name="watchlist")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)