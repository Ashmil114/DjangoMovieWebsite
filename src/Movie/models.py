from ast import arg
from audioop import reverse
from statistics import mode
from tkinter import CASCADE
from turtle import title
from django.db import models




CATEGORY_CHOICES = (
    ('ACTION','ACTION'),
    ('DRAMA','DRAMA'),
    ('COMEDY','COMEDY'),
    ('ROMANCE','ROMANCE')
)

LANGUAGE_CHOICE = (
    ('EN','ENGLISH'),
    ('MA','MALAYALAM'),
    ('TA','TAMIL'),
    ('HI','HINDI')

)

STATUS_CHOICE = (
    ('RA','RECENTLY ADDED'),
    ('MW','MOST WATCHED'),
    ('TR','TOP RATED')
)


class Movie(models.Model):
    title=models.CharField(max_length=100)
    descrition=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='movies')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=8)
    language=models.CharField(choices=LANGUAGE_CHOICE,max_length=2)
    status=models.CharField(choices=STATUS_CHOICE,max_length=2)
    year_of_production=models.DateField()
    view_count=models.URLField() #This is For Trailer URL
    
    

    def __str__(self):
        return self.title
    
    

