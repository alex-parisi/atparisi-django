from django.db import models


class Project(models.Model):

    # Header Info
    title = models.CharField(max_length=100)
    description = models.TextField()
    details = models.TextField()
    technology = models.CharField(max_length=20)
    link = models.URLField()
    image = models.FilePathField(path="/img")

    project_content = models.CharField(max_length=100)

    def __str__(self):
        return self.title
