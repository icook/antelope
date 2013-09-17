from yota.nodes import *
import yota
from yota.validators import *

class ImportForm(yota.Form):
    title = "CSV Import"
    data = TextareaNode(placeholder="Entery your CSV information here")
    simulate = CheckNode(checked=True)
    submit = SubmitNode()


class NewEntry(yota.Form):
    title = "Add a new entry"
    location = AutocompleteNode()
    total = EntryNode()
    cateogyr = EntryNode()
    note = TextareaNode()
    submit = SubmitNode()
