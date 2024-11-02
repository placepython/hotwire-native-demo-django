# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("one/", views.one, name="one"),
    path("two/", views.two, name="two"),
    path("long/", views.long, name="long"),
    path("scroll/", views.scroll, name="scroll"),
    path("follow/", views.follow, name="follow"),
    path("redirected/", views.redirected, name="redirected"),
    path("reference/", views.reference, name="reference"),
    path("files/", views.files, name="files"),
    path("new/", views.new, name="new"),
    path("bridge-form/", views.bridge_form, name="bridge_form"),
    path("bridge-menu/", views.bridge_menu, name="bridge_menu"),
    path("bridge-overflow/", views.bridge_overflow, name="bridge_overflow"),
    path("success/", views.success, name="success"),
    path("numbers/", views.numbers, name="numbers"),
    path("nonexistent/", views.nonexistent, name="nonexistent"),
    path("reference/turbo-drive/", views.turbo_drive, name="turbo_drive"),
    path("reference/turbo-frames/", views.turbo_frames, name="turbo_frames"),
    path("reference/turbo-streams/", views.turbo_streams, name="turbo_streams"),
    path("reference/turbo-native/", views.turbo_native, name="turbo_native"),
    path("protected/", views.protected, name="protected"),
    path("signin/", views.signin, name="signin"),
    path("slow/", views.slow, name="slow"),
    path("test/", views.test, name="test"),
]