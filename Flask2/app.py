from flask import Flask
from views.item import item
from views.category import category
from views.index import index
from views.cart import cart

app = Flask(__name__)

app.add_url_rule('/item', view_func = item )

app.add_url_rule('/category/<nameCategory>', view_func = category )

app.add_url_rule('/cart', view_func = cart )

app.add_url_rule('/', view_func = index )


if __name__ == "__main__":
    app.run(debug=True)