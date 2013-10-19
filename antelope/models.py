from flask import Flask, Blueprint, render_template, url_for, request
from antelope import db

import datetime

class Entry(db.Document):
    id = db.ObjectIdField()
    created_at = db.DateTimeField(default=datetime.datetime.now)
    desc = db.StringField(max_length=1023, required=True)
    location = db.StringField(max_length=255)
    cat = db.StringField(max_length=255)
    date = db.DateTimeField(required=True)
    amount = db.DecimalField()

    def get_absolute_url(self):
        return url_for('post', id=self.id)

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['date'],
        'ordering': ['-created_at']
    }
