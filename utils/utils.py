from django.contrib.sessions.models import Session
from django.utils.timezone import now
from utils.constants import CATEGORY_GET, CustomExceptionMessages
from utils.exceptions import CategoryNotFound


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


def generate_choices_from_response(response):
    """
    generate choices tuple from response data
    """
    CATEGORY_CHOICES = []
    for category in response:
        CATEGORY_CHOICES.append((category["id"], category["name"]))
    return tuple(CATEGORY_CHOICES)


def get_choices():
    """
    get Product Category Key and Value
    """
    from requests import get

    response = get(CATEGORY_GET)
    if response.status_code == 200:
        return generate_choices_from_response(response)
    else:
        raise CategoryNotFound(CustomExceptionMessages.CATEGORY_GET_EXCEPTION.value)


def get_repository_star():
    """
    get github repository star count
    """
    from requests import get

    response = get("https://api.github.com/repos/mohit-trootech/Ecommerce-API").json()
    return response.get("stargazers_count")


def get_api_stats():
    """
    get api stats information
    """
    from ecommerce.models import ApiStats

    try:
        hit = ApiStats.objects.first().hit
    except AttributeError:
        ApiStats.objects.create()
        hit = ApiStats.objects.first().hit
    return hit
