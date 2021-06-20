from django.db import models

# Create your models here.


class form(models.Model):  
    
    save_code = models.TextField(max_length=32, primary_key=True)

    title = models.CharField(max_length=100, verbose_name = "Başlık", null=True)
    explonation = models.TextField(max_length=1000, verbose_name = "Açıklama", null=True)
    link = models.TextField(max_length=1000, verbose_name = "Link", null=True)
    email= models.EmailField(max_length=100, verbose_name = "Email", null=True)
    photo= models.ImageField(upload_to='uploads/',verbose_name="Resim",default="Ek dosya", null=True)

    def __str__(self):
        return self.title

    @property
    def getsavecode(self):
        return self.save_code


