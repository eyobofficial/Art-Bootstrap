"""This module contains a collection of random utilitiy functions."""

def get_session_key(request):
    """Returns a session key for the request."""
    if request.session.session_key is None:
        request.session.save()
    return request.session.session_key

