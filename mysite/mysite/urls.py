from django.contrib import admin
from django.urls import path, include, re_path
from myapp.views import index, acricles, archive, user, article, aa, slug, u_number, regex

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='ind'),
    path("acricles/", include("myapp.urls")),
    path("users/", user),
    path("article/<int:article_number>/", article, name="article"),
    path("article/<int:article_number>/archive/", aa),
    path("article/<int:article_number>/<slug:slug_text>", slug, name="slug_article"),
    path("users/<int:users_number>", u_number, name="user_number"),
    re_path(r"^(?P<text>[a-f+1-9]{4}[-]\w{6}$)", regex)
]
