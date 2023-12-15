from django.test import TestCase
from html.parser import HTMLParser  
import json
from django.http import HttpResponse
import requests

class TestPokemons(TestCase):
    # Тут тесты по главной странице
    def test_pokemonListView(self):
        response = (self.client.get('/pokemons/'))
        container_resp = response.context
        #print(f'Response вернул ответ {list(container_resp)}')
        self.assertEquals(response.status_code,200)

    # Тут тесты по проверке есть ли charmander
    def test_pokemonListView_EqualsIn(self):
        base_response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0').json()
        base_container = base_response['results']
        response = (self.client.get('/pokemons/'))
        container_resp = response.context['response']['results']
        test = []
        for i in range(len(base_container)):
            if(not base_container[i]['name']==container_resp[i]['name']):
                test.append(False)
                print(False)
                break
        if(not test):
            print(True)
        self.assertIn('charmander',response.content.decode())

    def test_pokemonListView_rederict(self):
        response = (self.client.get('/'))
        container_resp = response.content.decode('utf-8')
        # print(f'Response вернул ответ {(container_resp)}')
        # print(f'Response вернул ответ {response.status_code}')
        self.assertEquals(response.status_code,302)
    # Тут тест по фастбатлу
    # def test_fastBattleView(self):
    #     response = (self.client.get('/pokemons/fastbattle/'))
    #     container_resp = response.context
    #     #print(f'Response вернул ответ {(container_resp)}')
    #     self.assertEquals(response.status_code,200)
    # Тут тест по просмотру покемонов
    def test_getFromNamePokemonListView(self):
        response = (self.client.get('/pokemons/charmander'))
        container_resp = response.context['response']['name']
        container_resp_name = container_resp
        print(f'Тестируем NamePokemonListView')
        if (container_resp_name=='charmander'):
            print(True)
        else:
            print(False)
        self.assertEquals(response.status_code,200)
    # Тест по битве покемонов
    def test_pokemonBattle(self):
        response = (self.client.get('/pokemons/battle/pikachu/charmander'))
        container_resp = response.context['response']['first']
        container_resp_opp = response.context['response']['second']
        container_resp_name = container_resp[0]['name']
        container_opp_name = container_resp_opp[0]['name']
        # print(f'Response вернул ответ {(container_resp_name, container_opp_name)}')
        first_pokemon_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/pikachu').json()['name']
        second_pokemon_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/charmander').json()['name']
        # print(f'Битва покемона {first_pokemon_response} и {second_pokemon_response}')
        print(f'Тестирование test_pokemonBattle')
        if (container_resp_name==first_pokemon_response and container_opp_name==second_pokemon_response):
            print(True)
        else:
            print(False)
        
