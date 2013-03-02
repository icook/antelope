import datetime
from flask import Flask, Blueprint, render_template, url_for, request
import json
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

@app.route("/import", methods=['GET', 'POST'])
def from_csv():
    if request.method == 'POST':
        for line in request.form['data'].split('\n'):
            fields = line.split(",")
            Entry(amount=fields[0], desc=fields[1], date=datetime.datetime.strptime(fields[2], "%m/%d/%Y"), cat=fields[3]).save()
        return json.dumps(["success","Data successfully added to the database!"])
    return render_template('import.html')

@app.route("/last_month")
def month():
    return render_template('month.html', entries=Entry.objects)

@app.route("/")
def hello():
    return "Hello World!"

class Entry(db.Document):
    id = db.ObjectIdField()
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
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

if __name__ == "__main__":
    app.debug = True
    app.run()
