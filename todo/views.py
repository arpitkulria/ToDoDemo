from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from todo.models import ToDoPolls
from django.http import HttpResponseRedirect


def index(request):
    all_items = ToDoPolls.objects.all().order_by("-added_date")
    print(all_items)
    return render(request, 'todo/index.html', {
        "todo_items": all_items
    })


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["item"]
    ToDoPolls.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect('/todo')


@csrf_exempt
def delete_todo(request, id):
    ToDoPolls.objects.get(id=id).delete()
    return HttpResponseRedirect('/todo')
