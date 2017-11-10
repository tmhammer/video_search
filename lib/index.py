from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

class Index:

  def create(self):
    es.indices.create(index=self.name, body=self.mapping)

  def index(self, data):
    for entry in data:
      entry['creation_date'] = datetime.now()
      es.index(index=self.name, doc_type=self.doc_type, body=entry)

  def search(self, query_body):
    return es.search(index=self.name, body=query_body)