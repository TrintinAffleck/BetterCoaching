from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from coaches.models import Coach, Review
from .serializers import CoachSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/coaches'},
        {'GET': '/api/coaches/id'},
        {'POST': '/api/coaches/id/review'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},

    ]

    return Response(routes)

@api_view(['GET'])
def getCoaches(request):
    coaches = Coach.objects.all()
    serializer = CoachSerializer(coaches, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCoach(request, pk):
    coach = Coach.objects.get(display_name=pk)
    serializer = CoachSerializer(coach, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def coachReview(request, pk):
    coach = Coach.objects.get(id=pk)
    review = Review.objects.create(
        owner = request.user.profile,
        coach = coach
    )

    review.rating_value = request.data['rating_value']
    review.body = request.data['body']
    review.save()
    coach.get_average

    serializer = CoachSerializer(coach, many=False)
    return Response(serializer.data)