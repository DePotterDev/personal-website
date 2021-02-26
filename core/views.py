from django.shortcuts import render
import requests

def home(request):
    """ Home Page """
    response = requests.get('https://api.github.com/users/depotterdev/repos?per_page=5&sort=updated')
    repo = response.json()
    context = {'repo': repo, 'range': range(4)}
    return render(request, 'home.html', context)