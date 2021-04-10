from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index")



def result(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)


