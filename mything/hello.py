from preact import h, Component, render

class Hello(Component):
    def __init___(self):
        super().__init__()
        self.display = 'Hello'

    def render(self):
        return h('p', {}, self.display)
    
w = getattr(globals(), 'window', dict(HTMLElement=object))

class Element(w['HTMLElement']):
    def connectedCallback(self):
        mountPoint = w['document'].createElement('span')
        self.attachShadow({ 'mode': 'open' }).appendChild(mountPoint)
        render(h(App, {'page': self.getAttribute('page')}), mountPoint)
        
    def define(self):
        if 'customElements' not in w: return
        w['customElements'].define('mything-hello', Element, ["page"])

Element().define()
