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

    if datacontent == '오늘':
        today = "오늘 급식"

        return JsonResponse({
                'message': {
                    'text': today
                }
            })

    elif datacontent == '내일':
        tomorrow = "내일 급식"

        return JsonResponse({
                'message': {
                    'text': tomorrow
                }
            })

