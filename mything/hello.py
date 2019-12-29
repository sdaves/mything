from mything.preact import h, Component, render

class Hello(Component):
    def __init___(self):
        super().__init__()
        self.display = 'Hello'

    def render(self):
        return h('p', {}, self.display)
    
def mount(self):
    mountPoint = document.createElement('span')
    self.attachShadow({ 'mode': 'open' }).appendChild(mountPoint)
    render(h(App, {'page': self.getAttribute('page')}), mountPoint)
    
if 'window' in globals(): defineElement('mything-hello', ['page'], mount)
