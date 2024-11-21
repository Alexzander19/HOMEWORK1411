from django.db import models

# Create your models here.
# создайте модель Note с полями:
# title: Заголовок заметки (строка, максимальная длина 200 символов).
# content: Содержимое заметки (текстовое поле).
# created_at: Дата создания заметки (автоматически создаваемое поле).

class Note(models.Model):
    title = models.CharField(max_length=200)
    conent = models.TextField()
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title 
    # Я наконец-то увидел зачем мы пишем __STR__