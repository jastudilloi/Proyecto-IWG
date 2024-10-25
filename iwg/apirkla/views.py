from django.shortcuts import render
import json
import requests
from django.http import JsonResponse
from datetime import datetime
import pytz

def temp_valpo(request):
    
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
        hora_utc = datosjson.get('datos', {}).get('valoresMasRecientes', {}).get('momento')
        if temp is None:
            return JsonResponse({"error": "No se pudo obtener la temperatura para la estación Valparaiso"}, status=404) 
        utc_formato = datetime.strptime(hora_utc, "%Y-%m-%d %H:%M:%S")
        zona= pytz.utc
        zonalocal= pytz.timezone('America/Santiago')
        utc_formato=zona.localize(utc_formato)
        hora=utc_formato.astimezone(zonalocal)
        horaformato=hora.strftime("registro tomado a las %H:%M:%S %d del %m de %Y")
        return JsonResponse({'temperatura': temp, 
                             'hora': horaformato
                             })
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def temp_viña(request):
    
    url = 'https://climatologia.meteochile.gob.cl/application/servicios/getEmaResumenDiario/320041'
    parametros= {
        'usuario': 'jastudilloi@usm.cl',
        'token': 'f131dbb15f42107af15d926d'  
    }
    
    try:
        respuesta = requests.get(url, params=parametros)
        respuesta.raise_for_status()
        datosjson = respuesta.json()
        temp = datosjson.get('datos', {}).get('valoresMasRecientes', {}).get('temperatura')
        hora_utc = datosjson.get('datos', {}).get('valoresMasRecientes', {}).get('momento')
        if temp is None:
            return JsonResponse({"error": "No se pudo obtener la temperatura para la estación Valparaiso"}, status=404)
        utc_formato = datetime.strptime(hora_utc, "%Y-%m-%d %H:%M:%S")
        zona= pytz.utc
        zonalocal= pytz.timezone('America/Santiago')
        utc_formato=zona.localize(utc_formato)
        hora=utc_formato.astimezone(zonalocal)
        horaformato=hora.strftime("registro tomado a las %H:%M:%S %d del %m de %Y")
        return JsonResponse({'temperatura': temp, 
                             'hora': horaformato
                             })
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    