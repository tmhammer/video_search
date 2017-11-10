from django.db import models
from datetime import datetime
from lib.index import Index

class Video(Index):
  name = 'video'
  doc_type = 'video'
  mapping = {
    'settings': {},
      'mappings': {
        'video': {
          'properties': {
            'title': { 'type': 'text'},
            'description': { 'type': 'text' },
            'creation_date': { 'type': 'date'},
            'tags': { 'type': 'keyword'}
          }
        }
      }
  }