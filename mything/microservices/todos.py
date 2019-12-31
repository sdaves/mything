import json

class Todos:
    def __init__(self, app, bottle):
        super().__init__()
        self._app = app
        self._bottle = bottle
        self._setup_run()
        
    def index(self):
        query = self._bottle.request.query
        return json.dumps(dict(data=[item+'='+query[item] for item in query]))
        
    def _setup_run(self):
        self._app.route('/todos')(lambda: self.index())
        self.run = self._app.run

if __name__ == '__main__':
    from dependencies import Injector
    import bottle as b
    class Container(Injector):
        todos = Todos
        app = b.Bottle()
        bottle = b
    Container.todos.run()
