from django.db import models

class New_title(models.Model):
    mini_title = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mini_title
        return self.title

class Entry(models.Model):
    new_title = models.ForeignKey(New_title, on_delete=models.CASCADE)
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."

