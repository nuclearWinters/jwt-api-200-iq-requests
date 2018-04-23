from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

import requests

class riotApiCall(APIView):
    def get(self, request):
        hola = {"Hola": "hey"}
        return Response(hola)

    def post(self, request):
        KEY = "RGAPI-a300d791-7d62-4b76-97fa-35056758367f"
        summonerName = request.data["summonerName"]
        url = "https://la1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName +"?api_key=" + KEY
        r = requests.get(url)
        if r.status_code == 200:    
            respuesta = r.json()
            respuesta = str(respuesta["id"])
            print(respuesta)
            url = "https://la1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/" + respuesta + "?api_key=" + KEY
            r = requests.get(url)
            if r.status_code == 200:
                respuesta = r.json()
                print(respuesta)
            else:
                respuesta = "No se encontro partida"
        else:
            respuesta = "No se encontro nombre de invocador"  
        return Response(respuesta)