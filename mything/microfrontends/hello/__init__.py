from mything.microfrontends.core import BaseFrontend

# __pragma__ ('js', '{}', 'setTimeout(()=>HelloFrontend(window.CustomHtml).define(),1)')

class HelloFrontend(BaseFrontend):    
    def __init__(self, html):
        super().__init__(html, 'mything-hello', ['name'], lambda x: self.mount(x))
        
    def render(self, props={'name':'Guest'}):
        return self._html.h('span', {}, 'Hello {0}!'.format(props['name']))
