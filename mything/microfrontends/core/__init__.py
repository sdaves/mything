# __pragma__ ('skip')
import typing
# __pragma__ ('noskip')

def mount(html, element, mountPoint, instance, attributes):
    attrs = dict()
    for item in attributes:
        attrs[item] = element.getAttribute(item)
    custom = instance.render(attrs)
    provider = html.h(html.ProppyProvider, {}, [custom])
    html.render(provider, mountPoint)    
    element.attachShadow({ 'mode': 'open' }).appendChild(mountPoint)

def define(fn, tag: str, attributes: []):
    # __pragma__ ('js', '{}', 'class cls extends HTMLElement{connectedCallback(){mount(window.CustomHtml, this, window.document.createElement("span"),fn(window.CustomHtml),attributes);}};window.customElements.define(tag, cls, attributes);')
    return fn

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
    
    def render(*args):
        pass
