# __pragma__ ('js', {}, __include__('./standalone.module.js'))

class Hello(Component):
    def __init___(self):
        super().__init__()
        self.display = 'Hello'

    def render(self):
        return h('p', {}, self.display)
    

if 'window' in globals():
    w = globals()['window']
    class cls(w.HTMLElement):
        def connectedCallback(self):
            mountPoint = w.document.createElement('span')
            self.attachShadow({ 'mode': 'open' }).appendChild(mountPoint)
            render(h(App, {'page': self.getAttribute('page')}), mountPoint)
    w.customElements.define('mything-hello', cls, ["page"]);
