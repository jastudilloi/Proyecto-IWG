from django.shortcuts import render
import json
import requests
from django.http import JsonResponse

def obtener_temp(request):
    
    url = 'https://climatologia.meteochile.gob.cl/application/servicios/getEmaResumenDiario/330007'
    parametros= {
        'usuario': 'jastudilloi@usm.cl',
        'token': 'f131dbb15f42107af15d926d'  
    }
    
    try:
        respuesta = requests.get(url, params=parametros)
        respuesta.raise_for_status()
        datosjson = respuesta.json()
        temp = datosjson.get('datos', {}).get('valoresMasRecientes', {}).get('temperatura')
        if temp is None:
            return JsonResponse({"error": "No se pudo obtener la temperatura para la estación Valparaiso"}, status=404)
        
        return JsonResponse({'temperatura': temp})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def verify(request):
    return JsonResponse({"mensaje": 'funciona waxo'})