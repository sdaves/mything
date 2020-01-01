import typing

class IHtml:
    def h(*args):
        pass
    
    def compose(*args):
        pass
    
    def withProps(*args):
        pass
    
    def withState(*args):
        pass 
    
    def attach(*args):
        pass 
    
class BaseElement:
    def __init__(self, html: IHtml, tag: str, attributes: [], mount: typing.Callable):
        super().__init__()
        self._html = html
        self._tag = tag
        self._attributes = attributes
        self._mount = mount        
        
    def define(self):
        if 'window' in globals(): 
            print('define', self._tag)
            # __pragma__ ('js', 'class cls extends HTMLElement{connectedCallback(){self._mount(this);}};window.customElements.define(self._tag, self._cls, self._attributes);')
        
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
        
    def render(self, props):
        return self._html.h('span', {}, 'render not implemented')

class CounterElement(BaseElement):    
    def __init__(self, html: IHtml):
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
    
if __name__ == '__main__': CounterElement(window.CustomHtml).define()
    
class HelloElement(BaseElement):    
    def __init__(self, html: IHtml):
        super().__init__(html, 'mything-hello', ['name'], lambda x: self.mount(x))
        
    def render(self, props={'name':'Guest'}):
        return self._html.h('span', {}, 'Hello {0}!'.format(props['name']))

if __name__ == '__main__': HelloElement(window.CustomHtml).define()
