from yota.nodes import *
import yota
from yota.validators import *

class ImportForm(yota.Form):
    title = "CSV Import"
    data = TextareaNode(placeholder="Entery your CSV information here")
    simulate = CheckboxNode(checked=True)
    submit = SubmitNode()
