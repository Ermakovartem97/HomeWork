from flask import render_template
from storage import getCategories

def cart():
    args = getCategories()
    return render_template('cart.html', nameCategory = args['nameCategory'])