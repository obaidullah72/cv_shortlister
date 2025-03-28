from django.db import models

class CV(models.Model):
    file = models.FileField(upload_to='cvs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CV uploaded on {self.uploaded_at}"