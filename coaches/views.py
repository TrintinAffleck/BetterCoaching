from django.shortcuts import render
from django.http import HttpResponse

coaches_list = [
    {
        "id": "1",
        "name": "Proctus",
        "description": "Insert Proctus description."
    },
    {
        "id": "2",
        "name": "Moriarty",
        "description": "Insert Moriaty description."
    },
    {
        "id": "3",
        "name": "Rabadon",
        "description": "Inser Rabadon description."
    },
    {
        "id": "4",
        "name": "Coach4",
        "description": "Coach 4 description."
    },
    {
        "id": "5",
        "name": "Coach5",
        "description": "Coach 5 desription."
    }
]

def coaches(request):
    context = {'coaches' : coaches_list}
    return render(request,'coaches_list.html', context)

def coach(request,pk):
    coachObj = None
    for i in coaches_list:
        if i['name'].lower() == pk.lower():
            coachObj = i
    if coachObj == None:
        return HttpResponse("Coach not found!")
    return render(request,'coach.html',{'coachObj' : coachObj})