class CustomElement:
    def __init__(self, html):
        super().__init__()
        self._html = html
        
    def config(self):
        return self._html.compose()

    def mount(self, element):
        mountPoint = window.document.createElement('span')
        element.attachShadow({ 'mode': 'open' }).appendChild(mountPoint)
        attrs = dict()
        for item in self.attributes:
            attrs[item] = element.getAttribute(item)
        custom = self._html.h(self._html.attach(self.config())(self.render), attrs)
        self._html.render(custom, mountPoint)    

class Hello(CustomElement):
    attributes = ['page']
    
    def __init__(self, html):
        super().__init__(html)
        self._html = html
        
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

if 'window' in globals(): window.defineElement('mything-hello', Hello.attributes, lambda x: Hello().mount(x))
