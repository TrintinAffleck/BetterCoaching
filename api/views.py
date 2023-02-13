from django.http import JsonResponse

def getRoutes(request):
    routes = [
        {'GET':'/api/coaches'},
        {'GET':'/api/coaches/id'},
        {'POST':'/api/coaches/id/review'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},

    ]

    return JsonResponse(routes, safe=False, json_dumps_params={'indent' : 2, 'sort_keys' : True})

