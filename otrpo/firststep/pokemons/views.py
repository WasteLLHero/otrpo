from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
import requests
from rest_framework import generics
from .forms import SearchPokemons

# def dataFromApi(request):
#         response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0').json()
#         return render(request,"pokemons.html", {"response":response}) 

class pokemonListView(View):
    def get(self, request):
        print(f"REQUEST ======== : {request}")
        search = request.GET.get('searchTAG','')
        print(f"вы ищите: {search}")

        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0').json()
        return render(request,"pokemons.html", {"response":response}) 

class getFromNamePokemonListView(View):
    def get(self, request, slug):
        print(f"REQUEST ======== : {slug}")
        pokemonName = slug
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{slug}').json()
        
        print("DATA === ", response)
        return render(request,"pokemonsName.html", {"response":response}) 

 