from django.db import models

class recipe(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    timetaken=models.IntegerField()
    image=models.ImageField(upload_to='images')

    def __str__(self):
        return self.title + "-" + str(self.timetaken)

