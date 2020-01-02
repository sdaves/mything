from mything.microfrontends.core import IFrontend

# __pragma__ ('js', '{}', 'setTimeout(()=>CounterFrontend(window.CustomHtml).define(),1)')

class CounterFrontend(IFrontend):    
    def __init__(self, html):
        super().__init__(html, 'mything-counter', ['page'], lambda x: self.mount(x))
        
    def config(self):
        return self._html.compose(
            self._html.withProps({'page': 'Home'}),
            self._html.withState('counter', 'setCounter', 0)
        )

    def render(self, props={'page':'Home', 'counter':0, 'setCounter':lambda x: None}):
        return self._html.h('div', {}, [
            props['page'], 
            props['counter'], 
            self._html.h('button', {'onClick': lambda: props['setCounter'](props['counter']+1)}, '+1')
        ])
