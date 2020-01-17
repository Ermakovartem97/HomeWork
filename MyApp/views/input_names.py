from flask import render_template, request

def input_names():
    error1 = None
    error2 = None
    print(request.method)
    if request.method == 'POST':
        username = request.form.get('username')
        users = username.split(',')
        if users:
            return render_template('print_names.html',users = users)
        else:
            error1 = 'Необходимо ввести имя пользоввателя'
        return render_template('input_name.html', error=error1)

    elif request.method == 'GET':
        username = request.args.get('username')
        users = username.split(',')
        if users:
            return render_template('print_names.html', users=users)
        else:
            error2 = 'Необходимо ввести имя пользоввателя'
        return render_template('input_name.html', error = error2)