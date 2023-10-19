from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
import requests
from rest_framework import generics
from .forms import SearchPokemons
import random

DB_HOST = "localhost"
DB_NAME = "pokemons"
DB_USER = "postgres"
DB_PASS = ""

import psycopg2
import psycopg2.extras
class DataBaseConnection:
    def __init__(self, DB_HOST,DB_NAME, DB_USER, DB_PASS):
        self.DB_HOST = DB_HOST
        self.DB_NAME = DB_NAME
        self.DB_USER = DB_USER
        self.DB_PASS = DB_PASS
    def createConnection(self):
        try:
            return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        except Exception as Exp:
            print(f"Ошибка... соединение не было установленно. {Exp}")
    def querry(self,connect,QUERRY):
        try:
            with connect:
                with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute(QUERRY)
                    return(cur.fetchall())
                
        except Exception as Exp:
            print("Запрос не выполнен! ", Exp)
    def CloseConnection(self,connect):
        try:
            connect.close()
        except Exception as Exp:
            print("Ошибка, нельзя закрыть не открытое подключение.")

    def addRez(self,connection,rez):
        cursor = connection.cursor()
        postgres_insert_query = f'INSERT INTO "fight_rezult" ("rezult") VALUES ({1})'
        record_to_insert = ((rez))
        cursor.execute(postgres_insert_query,record_to_insert)
        connection.commit()

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
        new_result = {'results':[]}
        for pok in rez:
            print(f"Ваш рез - {pok['name']}")
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
        con = DataBaseConnection
        connect = DataBaseConnection.createConnection(con)
        test2 = final
        test2 = ",".join(test2)
        print((test2))
        print(final)
        #q = con.querry(connect,connect=connect,QUERRY=f'INSERT INTO "fight_rezult" ("rezult") VALUES ({test2})')
        q = con.addRez(con,connect,test2)
        close = DataBaseConnection.CloseConnection(connect, connect)
        return test
class pokemonBattle(View):
    def get(self, request, slug):
        random.seed(100)
        print(f"REQUEST2 ========:{slug}")

        damage_from_user = request.GET.get('_fight','')
        print(f"Урон - {damage_from_user}")
        
        start = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0').json()
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{slug}').json()
        opponent_pokemon = random.choice(start['results'])
        opponent_pokemon_name = opponent_pokemon['name']
        opponent_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{opponent_pokemon_name}').json()
        test = {'first': 
                    (response['forms']+response['abilities']+response['stats']
                     +[{'img': response['sprites']['front_default']}]), 
                'second': 
                    (opponent_response['forms']+opponent_response['abilities']
                     +opponent_response['stats']+[{'img':opponent_response['sprites']['front_default']}])
        }
        print(test)

        if(slug=='1'):
            test = fight(response,opponent_response,damage_from_user,response['stats'],opponent_response['stats'])
            return render(request,"battle.html", {"response":test}) 
        return render(request,"battle.html", {"response":test}) 


    
 