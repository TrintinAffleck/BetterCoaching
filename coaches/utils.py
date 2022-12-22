
from django.db.models import Q
from users.models import Profile
from .models import Coach, Accomplishments


def search_coaches(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    accomplishments = Accomplishments.objects.filter(name__icontains=search_query)
    rank = Profile.objects.filter(rank__icontains=search_query)
    print(search_query)
    print(f"Search: {rank}")
    coach_obj = Coach.objects.filter(
    Q(display_name__icontains=search_query) |
    Q(body__icontains=search_query) |
    Q(accomplishments__in=accomplishments) |
    Q(headline=search_query) |
    Q(user_type__in=rank)
    )
    return coach_obj, search_query