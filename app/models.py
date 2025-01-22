from django.db import models

class Todo(models.Model):
    class Status(models.TextChoices):
        CREATED = 'C', 'Создан'
        IN_PROGRESS = 'P', 'В процессе'
        DONE = 'D', 'Завершен'
        CANCELED = 'X', 'Отменен'
    
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.CREATED)
    created_at = models.DateTimeField(auto_now_add=True)
    
    