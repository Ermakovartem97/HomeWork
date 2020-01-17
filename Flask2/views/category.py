from flask import render_template
from storage import getCategories

def category(nameCategory):
    args = getCategories()
    return render_template('category.html', nameCategorys = args['nameCategory'], nameCategory = nameCategory)