
from msilib.schema import ListView
from multiprocessing import context
from pyexpat import model
from turtle import title
from unicodedata import category, name
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


# Create your views 


def MovieList(request):
    movie_list={
        'list': Movie.objects.all()
    }
    return render(request,'movie_list.html',movie_list)

# def MovieDetail(request,movie_id):
#     # movie_object =Movie
#     get_movie=Movie.objects.filter(id=movie_id)
#     return render(request,'movie_detail.html',{'movie':get_movie})


# MOVIE CATEGORY
def MovieAction(request):
    action_list={
        'act_list': Movie.objects.all()
    }
    return render(request,'action_movies.html',action_list)

def MovieComedy(request):
    comedy_list ={
        'com_list' : Movie.objects.all()
    }
    return render(request,'comdey_movies.html',comedy_list)

def MovieRomance(request):
    romance_list ={
        'rom_list' : Movie.objects.all()
    }
    return render(request,'romance_movies.html',romance_list)

def MovieDrama(request):
    drama_list ={
        'dra_list' : Movie.objects.all()
    }
    return render(request,'drama_movies.html',drama_list)
# MOVIE CATEGORY END

# LANGUAGE 
def Movie_Lang_Eng(request):
    english_list={
        'eng_list' : Movie.objects.all()
    }
    return render(request,'eng_movies.html',english_list)

def Movie_Lang_Hin(request):
    hindi_list={
        'hin_list' : Movie.objects.all()
    }
    return render(request,'hin_movies.html',hindi_list)

# LANGUAGE END

#SEARCH



def Search(request):
    query= request.GET.get("query")
    searchMov={
        'smov' : Movie.objects.all(),
        'query':query.lower()
         
    }
    return render(request,'SearchMov.html',searchMov)



def MovieDetail(request,movie_id):
    # movie_object =Movie
    get_movie=Movie.objects.filter(id=movie_id)
    return render(request,'TrailerWatch.html',{'movie':get_movie})