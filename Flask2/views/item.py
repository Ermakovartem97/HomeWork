from flask import render_template
from storage import getCategories

def item():
    args = getCategories()
    return render_template('item.html', nameCategory = args['nameCategory'])