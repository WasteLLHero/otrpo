from django.contrib import admin
from django.urls import include, path
from pokemons import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemons/fastbattle/',views.fastbattleView.as_view()),
    path('social-auth/', include('social_django.urls')),

    #path('pokemons/',views.dataFromApi, name="pokemons"),

]
