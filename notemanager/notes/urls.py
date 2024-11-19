# '': Для отображения списка заметок.
# 'add/': Для добавления новой заметки.
# 'delete/<int:id>/': Для удаления заметки.

from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_notes, name="list_notes"),

    path("add/", views.add_notes, name="add_notes"),

    path("delete/<int:note_id>", views.delete_note, name="delete_note")

]