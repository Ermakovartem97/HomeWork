from flask import render_template
from storage import getCategories, getNameProduct

def index():
    args = getCategories()
    print(args)
    args.update(getNameProduct())
    print(args)
    return render_template('index.html', nameCategory = args['nameCategory'], nameProducts = args['nameProduct'])