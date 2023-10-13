from django import forms

class SearchPokemons(forms.Form):
    Search = forms.CharField(label='srth', max_length=100)
    print("Ты ввели значение: ")