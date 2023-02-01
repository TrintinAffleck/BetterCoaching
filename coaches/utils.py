from django.db.models import Q
from users.models import Profile
from .models import Coach, Accomplishments
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def search_coaches(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    accomplishments = Accomplishments.objects.filter(name__icontains=search_query)
    rank = Profile.objects.filter(rank__icontains=search_query)
    coach_obj = Coach.objects.filter(
    Q(user_type__in=rank) |
    Q(display_name__icontains=search_query) |
    Q(headline=search_query) |
    Q(body__icontains=search_query) |
    Q(accomplishments__in=accomplishments)
    )
    return coach_obj, search_query

def paginate_coaches(request, coaches, coaches_per_page):

    page = request.GET.get('page')
    paginator = Paginator(coaches, coaches_per_page)
    try:
        coaches = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        coaches = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        coaches = paginator.page(page)   
    
    left = (int(page)-3)
    if left < 1:
        left = 1

    right = (int(page)+3)
    if right > paginator.num_pages:
        right = paginator.num_pages+1

    custom_range = range(left,right)

    return custom_range, coaches