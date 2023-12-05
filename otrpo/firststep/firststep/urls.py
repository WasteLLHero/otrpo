
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
    path('Redis/<int:number>',views.RedisPaginationListView.as_view(), name="RedisView"),

    path('', include('social_django.urls')),


    path('registrations', views.signup, name='register_user'),
    path(r'^dashboard/$', views.dashboard, name='dashboard'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

    path('accounts/',include('django.contrib.auth.urls'), name="acc"),
    path('accounts/registration', views.SignUpView.as_view()),
    path(r'', include('social_django.urls')),


    path('pokemons/<slug:slug>',views.getFromNamePokemonListView.as_view()),
    path('pokemons/battle/<slug:slug>/<slug:name>',views.pokemonBattle.as_view(), name='pokemon_battle'),
]
