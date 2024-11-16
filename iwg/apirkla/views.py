from django.shortcuts import render
import json
import requests
from django.http import JsonResponse
from datetime import datetime
import pytz
import pandas as pd
import os
import random

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
            return JsonResponse({"error": "No se pudo obtener la temperatura para la estación Valparaíso"}, status=404) 
        
        utc_formato = datetime.strptime(hora_utc, "%Y-%m-%d %H:%M:%S")
        zona = pytz.utc
        zonalocal = pytz.timezone('America/Santiago')
        utc_formato = zona.localize(utc_formato)
        hora = utc_formato.astimezone(zonalocal)
        horaformato = hora.strftime("Registro tomado a las %H:%M:%S %d del %m de %Y")
        hora_obj = datetime.strptime(horaformato, "registro tomado a las %H:%M:%S %d del %m de %Y")
        fecha_formato = hora.strftime("%d-%b").lstrip("0").capitalize()
        
        archivocsv = os.path.join(os.path.dirname(__file__), 'TemperaturasMediasyExtremasen30Años_2024-11-15_22_52.csv')
        df = pd.read_csv(archivocsv)
        
        df['Dia-Mes'] = df['Dia-Mes'].str.lower().str.strip()
        fecha_formato = fecha_formato.lower()
        
        temperaturamedia = 'No Disponible'
        for _, fila in df.iterrows():
            if fila['Dia-Mes'] == fecha_formato:
                temperaturamedia = fila['Temperatura media']
                break

        mensajes = [
            "El agua es vida, no la desperdicies.",
            "Planta un árbol, siembra un futuro.",
            "La basura no desaparece, recíclala.",
            "Cuida la Tierra, es el único hogar que tenemos.",
            "La naturaleza no es un lujo, es nuestra necesidad.",
            "Camina más, contamina menos.",
            "Reutiliza, reduce, recicla.",
            "Proteger la biodiversidad es protegernos a nosotros mismos.",
            "El cambio climático es real, actúa ahora.",
            "Aprovecha la energía del sol, no la desperdicies.",
            "El océano no es un basurero, cuídalo.",
            "Sin abejas no hay vida.",
            "El mejor momento para cuidar el planeta fue ayer, el segundo mejor es hoy.",
            "Apaga las luces, enciende la conciencia.",
            "Arreglar es mejor que reemplazar.",
            "Cambia el auto por la bicicleta, el planeta te lo agradecerá.",
            "Consume local, piensa global.",
            "Respeta el aire, es lo que respiras.",
            "El cuidado del medio ambiente empieza contigo.",
            "El planeta no necesita más gente indiferente, necesita más cuidadores."
        ]
        
        mensajito=random.choice(mensajes)
        return render(request, 'valpo.html', {
            'temperatura': round(float(temp),1),
            'hora': horaformato,
            'media': temperaturamedia,
            'mensajito': mensajito,
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
            return JsonResponse({"error": "No se pudo obtener la temperatura para la estación Viña del Mar"}, status=404)
        
        utc_formato = datetime.strptime(hora_utc, "%Y-%m-%d %H:%M:%S")
        zona = pytz.utc
        zonalocal = pytz.timezone('America/Santiago')
        utc_formato = zona.localize(utc_formato)
        hora = utc_formato.astimezone(zonalocal)
        horaformato = hora.strftime("registro tomado a las %H:%M:%S %d del %m de %Y")
        hora_obj = datetime.strptime(horaformato, "Registro tomado a las %H:%M:%S %d del %m de %Y")
        
        fecha_formato = hora.strftime("%d-%b").lstrip("0").capitalize()
        
        archivocsv = os.path.join(os.path.dirname(__file__), 'TemperaturasMediasyExtremasen30Años_2024-11-15_22_52.csv')
        df = pd.read_csv(archivocsv)
        
        df['Dia-Mes'] = df['Dia-Mes'].str.lower().str.strip()
        fecha_formato = fecha_formato.lower()
        
        temperaturamedia = 'No Disponible'
        for _, fila in df.iterrows():
            if fila['Dia-Mes'] == fecha_formato:
                temperaturamedia = fila['Temperatura media']
                break
        
        mensajes = [
            "El agua es vida, no la desperdicies.",
            "Planta un árbol, siembra un futuro.",
            "La basura no desaparece, recíclala.",
            "Cuida la Tierra, es el único hogar que tenemos.",
            "La naturaleza no es un lujo, es nuestra necesidad.",
            "Camina más, contamina menos.",
            "Reutiliza, reduce, recicla.",
            "Proteger la biodiversidad es protegernos a nosotros mismos.",
            "El cambio climático es real, actúa ahora.",
            "Aprovecha la energía del sol, no la desperdicies.",
            "El océano no es un basurero, cuídalo.",
            "Sin abejas no hay vida.",
            "El mejor momento para cuidar el planeta fue ayer, el segundo mejor es hoy.",
            "Apaga las luces, enciende la conciencia.",
            "Arreglar es mejor que reemplazar.",
            "Cambia el auto por la bicicleta, el planeta te lo agradecerá.",
            "Consume local, piensa global.",
            "Respeta el aire, es lo que respiras.",
            "El cuidado del medio ambiente empieza contigo.",
            "El planeta no necesita más gente indiferente, necesita más cuidadores."
        ]
        
        mensajito=random.choice(mensajes)
        
        return render(request, 'vina.html', {
            'temperatura': round(float(temp),1),
            'hora': horaformato,
            'media': temperaturamedia,
            'mensajito': mensajito,
        })

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)