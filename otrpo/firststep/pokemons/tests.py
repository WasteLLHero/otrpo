from django.test import TestCase

class TestPokemons(TestCase):
    # Тут тесты по главной странице
    def test_pokemonListView(self):
        response = (self.client.get('/pokemons/'))
        print(f'Response вернул ответ {response.status_code}')
        self.assertEquals(response.status_code,200)
    def test_pokemonListView_EqualsIn(self):
        response = (self.client.get('/pokemons/'))
        self.assertIn('charmander',response.content.decode())

    def test_pokemonListView_rederict(self):
        response = (self.client.get('/'))
        print(f'Response вернул ответ {response.status_code}')
        self.assertEquals(response.status_code,302)
    # Тут тест по фастбатлу
    def test_fastBattleView(self):
        response = (self.client.get('/pokemons/fastbattle/'))
        print(f'Response вернул ответ {response.status_code}')
        self.assertEquals(response.status_code,200)
    # Тут тест по просмотру покемонов
    def test_getFromNamePokemonListView(self):
        response = (self.client.get('/pokemons/charmander'))
        print(f'Response вернул ответ {response.status_code}')
        self.assertEquals(response.status_code,200)
    # Тест по битве покемонов
    def test_pokemonBattle(self):
        response = (self.client.get('/pokemons/battle/pikachu/charmander'))
        print(f'Response вернул ответ {response}')
        self.assertEquals(response.status_code,200)

    
    #Тут тест по RedisPagination
    # def test_RedisPagination(self):
    #     response = (self.client.get('Redis/1'))
    #     print(f'Response вернул ответ {response.status_code}')
    #     self.assertEquals(response.status_code,200)