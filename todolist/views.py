from turtle import title
from unicodedata import category
from django.shortcuts import render,redirect
from .models import TodoList,Category

# Create your views here.

def index(request):
    todos = TodoList.objects.all() # quering all todos with the object manager
    categories= Category.objects.all() # quering all categories with object manager
    
    if request.method == "POST": # checking if the request method is a POST
        if "taskAdd" in request.POST: # checking if there is a request to add a todo
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_selelct"]
            content = title + " -- " + date + " " + category 
            Todo = TodoList(title=title, content = content, due_date = date, category=Category.objects.get(name=category))
            Todo.save()
            return redirect("")

        if "taskDelete" in request.POST: # checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] # checked todos  to be deleted

            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) # getting todo id
                todo.delete()
    
    return render(request, "index.html",{"todos" : todos, "categories" : categories})