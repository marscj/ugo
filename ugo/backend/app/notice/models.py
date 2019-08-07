from django.db import models

class Notice(models.Model):
    title = models.CharField(blank=True, null=True, max_length=128)
    subtitle = models.CharField(blank=True, null=True, max_length=256)
    create_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'notice'
    
    def __str__(self):
        return self.title
