from django.shortcuts import render
import json
import requests

def CurseAll(request):
    curse_list = requests.get(' https://currate.ru/api/?get=rates&pairs=USDRUB,EURRUB&key=2102f5cb9b1567fe5cfc773da35a830c')
    curse_list = curse_list.loads()
    return render(request, 'main/document_all_views.html', {'valuteAll': curse_list})
