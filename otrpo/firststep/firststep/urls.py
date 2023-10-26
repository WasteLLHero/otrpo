
from django.contrib import admin
from django.urls import include, path
from pokemons import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pokemons.urls")),
    path('fastbattle/',views.fastbattleView.as_view()),

    path('pokemons/',views.pokemonListView.as_view(), name="pokemonsList"),
    path('pokemons/<slug:slug>',views.getFromNamePokemonListView.as_view()),
    path('pokemons/battle/<slug:slug>/<slug:name>',views.pokemonBattle.as_view(), name='pokemon_battle'),
]
