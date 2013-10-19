from flask import Flask, Blueprint, render_template, url_for, request
from antelope import db, app
from antelope.models import Entry
from antelope.forms import NewEntry

import json
import datetime

@app.route("/entry/<id>")
def entry(id):
    entry = Entry.objects.get_or_404(id=id)
    return render_template('single_entry.html', entry=entry)

@app.route("/import", methods=['GET', 'POST'])
def from_csv():
    form = ImportForm()

    if request.method == 'POST':
        for line in request.form['data'].split('\n'):
            fields = line.split(",")
            Entry(amount=fields[0],
                  desc=fields[1],
                  date=datetime.datetime.strptime(fields[2], "%m/%d/%Y"),
                  cat=fields[3]).save()
        return json.dumps(["success","Data successfully added to the database!"])
    return render_template('import.html')

@app.route("/last_month")
def month():
    return render_template('month.html', entries=Entry.objects)

@app.route("/add", methods=['GET', 'POST'])
def new():
    form = NewEntry()
    locations = Entry.objects.distinct("location")
    form.location.json_autolist = json.dumps(locations)
    cat = Entry.objects.distinct("cat")
    form.category.json_autolist = json.dumps(cat)

    if request.method == 'POST':
        if form.validate_render(request.form):
            data = form.data_by_attr()
            entry = Entry(amount=data['total'],
                          desc=data['note'],
                          cat=data['category'],
                          date=datetime.datetime.now())
            entry.save()
            form.start.add_error({"message": "Successfully inserted new record",
                            "type": "success"})
    else:
        out = form.render()
    return render_template('new_entry.html', entry_form=form.render())


@app.route("/")
def hello():
    #entry = Entry.objects.sort({
    return render_template('home.html')
