from pyramid.view import view_config
from tinydb import TinyDB, Query

db = TinyDB('app_db.json')

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'Pyramid Scaffold'}

@view_config(route_name='hello', renderer='templates/hello.jinja2')
def my_view_hello(request):
    print(dir(request))
    name = 'Guest'
    try:
        name = request.params['name']
    except Exception as err:
        print(err)
    return {'name': name}

@view_config(route_name='submit', renderer='templates/submit.jinja2')
def my_view_submit(request):
    name = request.params['name']
    email = request.params['email']
    db.insert({'name': name, 'email': email})
    return {
        'name': name,
        'email': email
        }

@view_config(route_name='list', renderer='templates/list.jinja2')
def my_view_list(request):
    rv = db.all()
    print(rv)
    return {'records': rv}