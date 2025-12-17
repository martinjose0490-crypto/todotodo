from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import TodoItem

def index(request):
    # Fetch all tasks from the database
    todos = TodoItem.objects.all().order_by('-created_at')
    return render(request, 'todo/index.html', {'todos': todos})

def add_todo(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        notes = request.POST.get('notes')
        TodoItem.objects.create(subject=subject, notes=notes)
    return redirect('index')

def delete_todo(request, item_id):
    item = get_object_or_404(TodoItem, id=item_id)
    item.delete()
    return redirect('index')