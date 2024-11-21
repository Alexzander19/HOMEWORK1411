from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Note

# Create your views here.
# note_list: Отображает список всех заметок.
# add_note: Позволяет добавлять новую заметку.
# delete_note: Удаляет выбранную заметку.

# urlpatterns = [
#     path("", views.list_notes, name="list_notes"),

#     path("add/", views.add_notes, name="add_notes"),

#     path("delete/<int:note_id>", views.delete_note, name="delete_note")

# ]


def list_notes(request):

    list = Note.objects.order_by("-created_at")[:5]
   
    
    context = {"list": list}
    # return HttpResponse("Привет! Это приложение Notes.views list_notes.")

    return render(request, 'notes\\note_list.html',context)

def add_notes(request):
     
    # HttpResponse("Привет! Это приложение Notes.views add_notes.")
    # return render(request, "admin/notes/note/add/")
    return HttpResponseRedirect('/admin/notes/note/add/')


def delete_note(request, note_id):

    # note_to_del = Note.objects.get(id = blog_id)
    # context = {"one_blog": note_to_del}
   
    # return HttpResponse(response % blog_id)
    # return HttpResponse("Привет! Это приложение Notes.views delete_notes.")
    # return render(request, "delete_note.html", context) 
    return HttpResponseRedirect(f'/admin/notes/note/{note_id}/delete/') 
