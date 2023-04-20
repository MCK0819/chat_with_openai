# chatbot/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import openai
import requests

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(messages):
    print(messages)
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai.api_key}',
    }
    data = {
        'model': "gpt-3.5-turbo",
        'messages': [{"role":"user", "content": messages}],

        'max_tokens': 500,
        'temperature': 0,
        #'stream':False,
        #'logprobs': None,
        'top_p':1,

    }
    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    return response.json()['choices'][0]['message']['content'].strip()
    #return response.json()['error']['message'].strip()

def chatbot_response(request):
    if request.method == 'GET':
        # GET 요청에 대한 처리
        prompt = request.GET.get('message')
        response_text = generate_response(prompt)
        return JsonResponse({'response': response_text})
    else:
        # GET 요청 이외에 대한 처리
        return JsonResponse({'error': 'Invalid request method'})

def index(request):
    return render(request, 'chat.html')

