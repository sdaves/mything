class CounterFrontend:    
    def __init__(self, html):
        self._html = html
        
    def config(self):
        return self._html.compose(
            self._html.withProps({'page': 'Home'}),
            self._html.withState('counter', 'setCounter', 0)
        )

    def render(self, props={'page':'Home', 'counter':0, 'setCounter':lambda x: None}):
        root = self._html.h('div', {}, [
            props['page'], 
            props['counter'], 
            self._html.h('button', {'class':'pure-button pure-button-primary','onClick': lambda: props['setCounter'](props['counter']+1)}, '+1')
        ])
        return self.config()([root])