from django.db import models

# Create your models here.
class Invoice(models.Model):
    invoice_sig = models.CharField(max_length = 10)
    invoice_num = models.CharField(max_length = 10)
    invoice_date = models.DateField()
    tax = models.IntegerField()
    total = models.IntegerField()
    invoice_check_code = models.CharField(max_length = 100)
    file = models.FileField(upload_to='media/')

    def __str__(self) -> str:
        return self.invoice_check_code

class FileTool(models.Model):
    title = models.CharField(max_length = 255)
    link = models.TextField()

    def __str__(self) -> str:
        return self.title