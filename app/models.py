from __future__ import unicode_literals

from django.db import models

# notes-project/app/models.py

import os
import datetime
# import mongoengine
from mongoengine import Connect, Document, StringField, DateTimeField

# get the URI from environment variables
# uri = os.getenv('URI')
# connect to our database at AWS
# connect(host=uri)
uri = 'test'
connect(uri)

class Notebook(Document):
    '''
    this collection defines how our notes document will look like
    '''
    title = StringField(max_length=500, required=True) # Title of the note
    notes = StringField(max_length=500, required=True) # Details of the note
    date_modified = DateTimeField(default=datetime.datetime.now)

