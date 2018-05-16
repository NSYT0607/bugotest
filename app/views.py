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

    if datacontent in ('Comment tu t\'appelles?', 'Tu t\'appelles comment?'):
        today = "Je m’appelle Eva."

        return JsonResponse({
                'message': {
                    'text': today
                }
            })

    elif datacontent == 'Tu es d\'où?' or datacontent == 'Tu viens d\'où?' :
        tomorrow = "Je suis de Paris."

        return JsonResponse({
                'message': {
                    'text': tomorrow
                }
            })
    elif datacontent == 'Tu as quel âge?' :
        tomorrow = "J’ai 18 ans"

        return JsonResponse({
                'message': {
                    'text': tomorrow
                }
            })
    elif datacontent == 'Tu es française?' :
        tomorrow = " Oui, je suis française. Tu parles français?"

        return JsonResponse({
                'message': {
                    'text': tomorrow
                }
            })
    elif datacontent == 'Oui, un peu. Au revoir.' :
        tomorrow = "Au revoir."

        return JsonResponse({
                'message': {
                    'text': tomorrow
                }
            })
    else :
        response = "Faux! 잘못 입력하셨어요."

        return JsonResponse({
                'message': {
                    'text': response
                }
            })


