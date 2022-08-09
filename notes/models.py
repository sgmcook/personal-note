from django.db import models

class Note(models.Model):
    owner = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, default='')
    body = models.TextField(max_length=2000, null=True)
    archived = models.BooleanField(default=False)

    class Meta:
        ordering = ['pub_date']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
