from django.contrib.sessions.models import Session
from django.utils.timezone import now


def force_logout(request):
    """
    logout user from request
    """

    sessions = Session.objects.filter(expire_date__gt=now())

    for session in sessions:
        id = session.get_decoded().get("_auth_user_id")
        if id:
            if request.user.pk == int(id):
                session.delete()
