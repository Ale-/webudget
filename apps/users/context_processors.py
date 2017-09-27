def current_username(request):
    """Injects the name of current user in site-wide context"""

    current_username = request.user.username

    return { 'current_username' : current_username }
