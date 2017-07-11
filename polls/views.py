from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def details(request, question_id):
    return HttpResponse("Hello, you are on details page. %s" % question_id)

def results(request, question_id):
    return HttpResponse("Results Page %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Votes %s" % question_id)