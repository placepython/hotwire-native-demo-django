import time

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model, login

User = get_user_model()


def index(request):
    """Renders the home page with a specific title and page class."""
    return render(request, "index.html", {"title": "Hotwire Native Demo", "page_class": "index"})

def one(request):
    """Renders the 'one' page with a custom title."""
    return render(request, "one.html", {"title": "How’d You Get Here?"})

def two(request):
    """Renders the 'two' page with a title and action query parameter."""
    return render(request, "two.html", {"title": "Push or Replace?", "action": request.GET.get("action")})

def long(request):
    """Renders a long page to demonstrate scroll behavior."""
    return render(request, "long.html", {"title": "A Really Long Page"})

def scroll(request):
    """Renders the scroll page with a title."""
    return render(request, "scroll.html", {"title": "Restoring Your Scroll"})

def follow(request):
    """Redirects the user to the redirected page."""
    return redirect("redirected")

def redirected(request):
    """Renders a page to indicate the user has been redirected."""
    return render(request, "redirected.html", {"title": "Redirected Page"})

def reference(request):
    """Renders the reference page with a specific title and page class."""
    return render(request, "reference.html", {"title": "Reference", "page_class": "index"})

def files(request):
    """Renders the files handling page."""
    return render(request, "files.html", {"title": "Handling Files"})

@require_http_methods(["GET", "POST"])
def new(request):
    """Renders a modal webpage on GET; redirects to success on POST."""
    if request.method == "POST":
        return redirect("success")
    return render(request, "new.html", {"title": "A Modal Webpage"})

@require_http_methods(["GET", "POST"])
def bridge_form(request):
    """Renders the bridge form page on GET; redirects with delay on POST."""
    if request.method == "POST":
        time.sleep(1.5)
        return redirect("success")
    return render(request, "bridge-form.html", {"title": "Bridge Form"})

def bridge_menu(request):
    """Renders the bridge menu page."""
    return render(request, "bridge-menu.html", {"title": "Bridge Menu"})

def bridge_overflow(request):
    """Renders the bridge overflow page."""
    return render(request, "bridge-overflow.html", {"title": "Bridge Overflow"})

def success(request):
    """Renders the success page with a confirmation title."""
    return render(request, "success.html", {"title": "It Worked!"})

def numbers(request):
    """Renders a page displaying a list of numbers."""
    return render(request, "numbers.html", {"title": "A List of Numbers"})

def nonexistent(request):
    """Returns a 404 response indicating the page was not found."""
    return HttpResponseNotFound("Not Found")

def turbo_drive(request):
    """Renders the Turbo Drive reference page."""
    return render(request, "turbo-drive.html", {"title": "Turbo Drive"})

def turbo_frames(request):
    """Renders the Turbo Frames reference page."""
    return render(request, "turbo-frames.html", {"title": "Turbo Frames"})

def turbo_streams(request):
    """Renders the Turbo Streams reference page."""
    return render(request, "turbo-streams.html", {"title": "Turbo Streams"})

def turbo_native(request):
    """Renders the Turbo Native reference page."""
    return render(request, "turbo-native.html", {"title": "Turbo Native"})

def protected(request):
    """Renders a protected page if the user is authenticated; returns 401 if not."""
    if request.COOKIES.get("authenticated"):
        return render(request, "protected.html", {"title": "Protected Webpage"})
    else:
        return HttpResponse(status=401, content="Unauthorized")

@require_http_methods(["GET", "POST"])
def signin(request):
    """Renders the sign-in page on GET; sets authentication cookie and redirects on POST."""
    if request.method == "POST":
        username = request.POST.get("name")
        user, created = User.objects.get_or_create(username=username, defaults={"password": "changeme"})
        if created:
            user.set_password("changeme")
            user.save()
        login(request, user)
        return redirect("index")
    return render(request, "signin.html", {"title": "Sign In"})

def slow(request):
    """Renders a page with a delay to simulate slow loading."""
    time.sleep(3)
    return render(request, "slow.html", {"title": "Slow-loading Page"})

def test(request):
    """Returns a 200 OK status as a test response."""
    return HttpResponse(status=200)