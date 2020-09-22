from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def body_short(self):
        return self.body[:100]
