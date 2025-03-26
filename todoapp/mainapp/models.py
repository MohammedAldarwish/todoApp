from django.db import models

class TaskDb(models.Model):
    PRIORITY_CHOICES = [
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low')
    ]
    title = models.CharField(max_length=250)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title
