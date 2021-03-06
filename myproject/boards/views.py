from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Board,Topic,Post
from django.contrib.auth.models import User
from .forms import NewTopicForm

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

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # todo: get the currently logged in user
   
    # works fine
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  #todo: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})

#     #does not work
#     #Error: NOT NULL constraint failed: boards_topic.board_id
    # I guess that maybe this part is not correct itself, 
    # just for explaining the core processing of forms clearly, 
    # so eliminated other irrelevant parts of code
    # That's why the error occurs
# #     #grab data from html and start a new topic
    # if request.method == 'POST':
    #     form=NewTopicForm(request.POST)
    #     if form.is_valid():
    #         topic=form.save()
    #         return redirect('board_topics',pk=board.pk)
    # else:
    #     form=NewTopicForm()
    # return render(request,'new_topic.html',{'form':form})