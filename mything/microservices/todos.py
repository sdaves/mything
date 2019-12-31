import json

class Todos:
    def __init__(self, app, bottle):
        super().__init__()
        self._app = app
        self._bottle = bottle
        self._setup()
        
    def list(self):
        query = self._bottle.request.query
        return json.dumps(dict(data=[item+'='+query[item] for item in query]))
    
    def single(self, name):
        return json.dumps(dict(data=[name]))
    
    def _setup(self):
        self.run = self._app.run
        route = self._app.route
        route('/todos')(self.list)
        route('/todos/<name>')(self.single)

if __name__ == '__main__':
    from dependencies import Injector
    import bottle as b
    class Container(Injector):
        todos = Todos
        app = b.Bottle()
        bottle = b
    Container.todos.run()
