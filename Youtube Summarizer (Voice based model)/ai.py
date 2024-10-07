from config import key
import requests 
from requests import get
import audio2text

def chat1(query): 
    try:
        messages = []
        system_message = '''You are a video summurizer voice based model created by Shubham gupta a Computer Engineering Student. You are given the capbilities to summerize the traincibed data of any video . the summerization  should be under 30% of actual data.'''
        message= {  'role': 'User','parts': [{'text': system_message+' '+query}]}
        messages.append(message)
        data = {'contents': messages }
        url= 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key='+key
        response=requests.post(url,json=data)

        t1= response.json()
        t1=t1.get('candidates')[0].get('content').get('parts')[0].get('text')
        t1=t1.replace('*','')
        t1=t1.replace("'''","").replace('python',"")
        # print(t1)
    except Exception as e:
        return e
    
    return t1

def chat2(query):
    messages = []
    data= audio2text.data
    system_message = f'''{data}\n you have to answer the asked question based on this transcribed data and explain in simple language.'''
    message= {  'role': 'User','parts': [{'text': system_message+' '+query}]}
    messages.append(message)
    data = {'contents': messages }
    url= 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key='+key
    response=requests.post(url,json=data)

    t1= response.json()
    t1=t1.get('candidates')[0].get('content').get('parts')[0].get('text')
    t1=t1.replace('*','')
    t1=t1.replace("'''","").replace('python',"")
    # print(t1)

    return t1


