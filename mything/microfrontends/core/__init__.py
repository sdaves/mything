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
    
class BaseFrontend:
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
