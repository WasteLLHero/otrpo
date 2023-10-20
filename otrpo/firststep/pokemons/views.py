from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
import requests
from rest_framework import generics
from .forms import SearchPokemons
import random
from .models import fightRezult
# def dataFromApi(request):
#         response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0').json()
#         return render(request,"pokemons.html", {"response":response}) 

class pokemonListView(View):
    def get(self, request):
        print(f"REQUEST11 ======== : {request}")
        search = request.GET.get('searchTAG','')
        print(f"вы ищите: {search}")
        
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0').json()
        rez = response['results']
        opponent_pokemon = random.choice(rez)
        ch_for_fast_battle = random.choice(rez)
        o_name = opponent_pokemon['name']
        print(f"res =========== {rez}")
        for pok in rez:
            pok["opp"] = o_name
            pok["rand"] = ch_for_fast_battle
        new_result = {'results':[]}
        print(f"q = {response}")
        for pok in rez:
            #print(f"Ваш рез - {pok['name']}")
            if (search in pok['name']):
                new_result['results'].append(pok)
        if(search):
            return render(request,"pokemons.html", {"response":new_result}) 
        else: 
            return render(request,"pokemons.html", {"response":response}) 

class getFromNamePokemonListView(View):
    def get(self, request, slug):
        print(f"REQUEST ======== : {slug}")
        pokemonName = slug
        print(f"Имя -> {pokemonName}")
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{slug}').json()  
        #print("DATA === ", response)
        return render(request,"pokemonsName.html", {"response":response}) 
    

def fight(response,opponent_response,damage_from_user, u_stat, opp_stat):
        final = []
        damage_opponent = random.randint(1,10)
        print(f"Урон оппонента - {damage_opponent}")
        print(f"Урон вашего покемона - {damage_from_user}")
        if (damage_from_user!=0):
            print(u_stat)
            stat_matr, stat_matr_opp = [],[]
            for pok in u_stat:
                stat_matr.append(pok['base_stat'])
            for pok in opp_stat:
                stat_matr_opp.append(pok['base_stat'])
            if(int(damage_from_user)%2==damage_opponent%2):
                result_ = "Вы выиграли удар!"
                final.append(f"Вы выиграли удар, нанесенный урон {stat_matr[1]}")
                print("Вы выиграли удар!")
                stat_matr_opp[0]-=stat_matr[1]
                print(stat_matr_opp[0])
            else:
                result_ = "Вы проиграли удар!"
                final.append(f"Вы проиграли удар, полученный урон {stat_matr_opp[1]}")
                print("Вы проиграли удар!")
                print(f"Урон по вам - {stat_matr_opp[1]}")
                stat_matr[0]-=stat_matr_opp[1]
                print(stat_matr_opp[0])


            for pok in range(len(u_stat)):
                u_health = u_stat[pok]
                o_health = opp_stat[pok]
                u_health['base_stat'] = stat_matr[pok]
                o_health['base_stat'] = stat_matr_opp[pok]
            if(stat_matr[0]<=0):
                print("Вы проиграли бой")
                final.append("Вы проиграли бой!")
            elif(stat_matr_opp[0]<=0):
                final.append("Вы выиграли бой!")
                print("Вы выиграли бой")

            print(f"Ваши статы - {stat_matr}")
            print(f"Cтаты оппонента - {stat_matr_opp}")
            test = {'first': 
                        (response['forms']+response['abilities']+response['stats']
                        +[{'img': response['sprites']['front_default']}]), 
                    'second': 
                        (opponent_response['forms']+opponent_response['abilities']
                        +opponent_response['stats']+[{'img':opponent_response['sprites']['front_default']}]),
                    'final':final
            }
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",test)
            print(f"final -> {final}")
            text = final
            text = ",".join(text)
            rezult = fightRezult(rezult=text)
            rezult.save()
            return test
        test = {'first': 
                        (response['forms']+response['abilities']+response['stats']
                        +[{'img': response['sprites']['front_default']}]), 
                    'second': 
                        (opponent_response['forms']+opponent_response['abilities']
                        +opponent_response['stats']+[{'img':opponent_response['sprites']['front_default']}]),
                    'final':final
        }
        return test


class pokemonBattle(View):
    def get(self, request, slug,name):
        print(f"REQUEST2 ========:{slug}")
        damage_from_user = request.GET.get('_fight','')
        if(not damage_from_user):
            damage_from_user=0

        print(f"Урон - {damage_from_user}")
        start = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0').json()
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{slug}').json()
        opponent_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}').json()
        test = fight(response,opponent_response,damage_from_user,response['stats'],opponent_response['stats'])
        return render(request,"battle.html", {"response":test}) 

    
class fastbattleView(View):
    def get(self, request):
        start = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0').json()
        rez = start['results']
        first_pok = random.choice(rez)
        second_pok = random.choice(rez)
        print(f"Первый покемон - {first_pok}")
        first_pokemon_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{first_pok["name"]}').json()
        second_pokemon_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{second_pok["name"]}').json()
        first_ch = random.randint(1,10)
        second_ch = random.randint(1,10)
        final =[]
        if(first_ch>second_ch):
            final.append(f"Покемон {first_pok['name']} выиграл бой!")
        else:
            final.append(f"Покемон {second_pok['name']} выиграл бой!")

        test = {'first': 
                        (first_pokemon_response['forms']+first_pokemon_response['abilities']+first_pokemon_response['stats']
                        +[{'img': first_pokemon_response['sprites']['front_default']}]), 
                    'second': 
                        (second_pokemon_response['forms']+second_pokemon_response['abilities']
                        +second_pokemon_response['stats']+[{'img':second_pokemon_response['sprites']['front_default']}]),
                    'final':final
        }
        print(f"Второй покемон{test['second']}")

        text = ",".join(final)
        rezult = fightRezult(rezult=text)
        rezult.save()
        return render(request,"fastbattle.html", {"response":test}) 