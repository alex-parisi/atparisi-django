from django.db import models


class Project(models.Model):

    # Header Info
    title = models.TextField()
    description = models.TextField()
    details = models.TextField()
    technology = models.TextField()
    link = models.URLField()
    image = models.FilePathField(path="/img")
    tags = models.TextField()

    project_content = models.CharField(max_length=100)

    def __str__(self):
        return self.title
