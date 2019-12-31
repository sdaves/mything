from .lib import bottle, decouple

@bottle.route('/todos')
def index():
    return str(dict(data=[]))

if __name__ == '__main__':
    bottle.run()
