from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Board

# Create your views here.
def home(request):
    #list all the existing boards
    #rendering part will be done by the django template engine
    boards = Board.objects.all()
    # boards_names = list()
    # for board in boards:
    #     boards_names.append(board.name)
    # response_html = '<br>'.join(boards_names)
    # return HttpResponse(response_html)
    return render(request,'home.html',{'boards':boards})

def board_topics(request,pk):
    #if not raise error 404, simply using obj.get(), 
    #when encountering a non-existing board, the test will fail
    #and in production, the visitor will see 500 internal server error
    #which is not we want, we want to show 404 Page Not Found

    #sol1:
    # try:
    #     boards = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404 #this will show the default 404 page, later on we will customize it

    #sol2: this will do as well
    boards = get_object_or_404(Board,pk=pk)

    return render(request,'topics.html',{'board':boards})