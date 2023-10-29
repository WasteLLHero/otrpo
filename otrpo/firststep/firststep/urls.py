
from django.contrib import admin
from django.urls import include, path
from pokemons import views 
from django.views.generic.base import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pokemons.urls")),
    path('fastbattle/',views.fastbattleView.as_view()),
    path('',RedirectView.as_view(url='pokemons')),


    path('pokemons/',views.pokemonListView.as_view(), name="pokemonsList"),
    path('Radis/',views.RedisPaginationListView.as_view(), name="RedisView"),

    path('pokemons/<slug:slug>',views.getFromNamePokemonListView.as_view()),
    path('pokemons/battle/<slug:slug>/<slug:name>',views.pokemonBattle.as_view(), name='pokemon_battle'),
]
