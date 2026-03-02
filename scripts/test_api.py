import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','backend.settings')
import django
django.setup()
from django.test import Client
c=Client()
print('GET /api/profile/ ->', c.get('/api/profile/').status_code)
print('GET /api/projects/ ->', c.get('/api/projects/').status_code)
print('GET /api/academic/ ->', c.get('/api/academic/').status_code)
print('GET /api/technologies/ ->', c.get('/api/technologies/').status_code)
resp = c.post('/api/contact/', {'name':'Test','email':'t@example.com','subject':'Hello','message':'Hi'}, content_type='application/json')
print('POST /api/contact/ ->', resp.status_code)
print('POST response body:', resp.content)
