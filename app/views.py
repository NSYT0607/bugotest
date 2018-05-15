from django.shortcuts import render

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json



def keyboard(request):

    return JsonResponse({
        'type':'text'
    })

@csrf_exempt
def answer(request):

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == 'Comment tu t\'appelles?':
        today = "Je m'appelle 상연."

        return JsonResponse({
                'message': {
                    'text': today
                }
            })

    elif datacontent == 'Tu es d\'où?':
        tomorrow = "Je suis de Séoul."

        return JsonResponse({
                'message': {
                    'text': tomorrow
                }
            })

    else :
        response = "잘못 입력."

        return JsonResponse({
                'message': {
                    'text': response
                }
            })


