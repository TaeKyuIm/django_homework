from django.db import models
class Apply(models.Model):
    name = models.CharField(max_length=10)
    id = models.AutoField(primary_key=True)
    answer1 = models.TextField()
    answer2 = models.TextField()
    answer3 = models.TextField()
    answer4 = models.TextField()
    answer5 = models.TextField()

    def __str__(self):
        return self.name