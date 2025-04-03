from django.db import models

class CV(models.Model):
    STATUS_CHOICES = [
        ('Processed', 'Processed'),
        ('Pending', 'Pending'),
    ]
    file = models.FileField(upload_to='cvs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    extracted_text = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    entities = models.JSONField(blank=True, null=True)  

    def __str__(self):
        return f"CV uploaded on {self.uploaded_at}"