def native_app(request):
    user_agent = request.META.get("HTTP_USER_AGENT", "")
    return {
        "native_app": "Turbo Native" in user_agent
    }