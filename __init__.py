import datetime
from flask import Flask, Blueprint, render_template, url_for
from flask.ext.mongoengine import MongoEngine
from flask.views import MethodView

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config["MONGODB_SETTINGS"] = {'DB': "antelope_finance"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)
user = "isaac"

@app.route("/entry/<id>")
def entry(id):
    entry = Entry.objects.get_or_404(id=id)
    return render_template('single_entry.html', entry=entry)

@app.route("/import")
def from_csv():
    return render_template('import.html')

@app.route("/")
def hello():
    return "Hello World!"

class Entry(db.Document):
    id = db.ObjectIdField()
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    desc = db.StringField(max_length=1023, required=True)
    location = db.StringField(max_length=255, required=True)
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

if __name__ == "__main__":
    app.debug = True
    app.run()
