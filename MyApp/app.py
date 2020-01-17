from flask import Flask, request, render_template
from views.input_name import input_name
from views.input_names import input_names

app = Flask(__name__)

app.add_url_rule('/name', view_func = input_name, methods=['GET','POST'])
app.add_url_rule('/', view_func = input_names, methods=['GET','POST'])

if __name__ == '__main__':
    app.run()

