from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=100)
    authour = models.CharField(max_length=100)
    authour_image = models.ImageField(upload_to='AuthorImages')
    time = models.DateTimeField(auto_now_add=True, blank=True)
    tags = models.CharField(max_length=1000, blank=True)
    content = models.TextField()
    content_image = models.ImageField(upload_to='ContentImage')
    slug = models.SlugField(default=None)

    def __str__(self):
        return self.title

    def preview(self):
        return self.content[:250] + ' . . .'

    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"