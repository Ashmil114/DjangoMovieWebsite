
from django.urls import path
from Movie import  views

app_name='Movie'

urlpatterns = [
    path('', views.MovieList,name='home'),
    path('action',views.MovieAction,name='action'),
    path('comedy',views.MovieComedy,name='comedy'),
    path('romance',views.MovieRomance,name='romance'),
    path('drama',views.MovieDrama,name='drama'),
    path('english',views.Movie_Lang_Eng,name='eng'),
    path('hindi',views.Movie_Lang_Hin,name='hin'),
    # path('MovieDetail/<movie_id>',views.MovieDetail,name='movie_detail'),
    path('MovieDetail/<movie_id>',views.MovieDetail,name='TrailerWatch'),
    path('search/', views.Search,name='search'),

    
    

]

