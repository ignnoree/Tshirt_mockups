from django.db import models


#created tshirts table
class Mockup(models.Model):
    text = models.CharField(max_length=200)
    image_url = models.CharField(max_length=500, null=True, blank=True) 
    font = models.CharField(max_length=100, default="arial")
    text_color = models.CharField(max_length=7, default="#FFFFFF")
    shirt_color = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shirt_color} - {self.text}"
    

