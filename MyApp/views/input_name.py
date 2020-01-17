from flask import render_template, request

def input_name():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        if username:
            return render_template('print_name.html',name = username)
        else:
            error = 'Необходимо ввести имя пользоввателя'
    return render_template('input_name.html', error = error)

