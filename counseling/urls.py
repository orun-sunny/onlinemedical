from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from.import views


urlpatterns = [
    path("",views.index, name="home"),
    path("about/",views.about, name="about"),
    path("profile/<str:i>/",views.profile, name="profile"),
    path("profile_edit/",views.profile_edit, name="profile_edit"),
    path("base/",views.base, name="base"),
    path("<str:i>/post_write/",views.post_write, name="post_write"),

    path("blog/",views.blog, name="blog"),
    path("contact/",views.contact, name="contact"),
    path("department/",views.department, name="department"),
    path("blog_single/<str:i>/",views.blog_single, name="blog_single"),
    path("gallery/",views.gallery, name="gallery"),

    path("services/",views.services, name="services"),
    path("ProfileFilterView/",views.ProfileFilterView,name="ProfileFilterView"),
    path("search/",views.search,name="=search"),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
