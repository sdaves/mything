from dependencies import Injector
from mything.microfrontends.core import IHtml, webcomponent
from mything.microfrontends.hello.HelloFrontend import HelloFrontend

 # __pragma__ ('js', '{}', 'IHtml = window.CustomHtml')

class Container(Injector):
    html = IHtml
    hello = HelloFrontend
    
webcomponent('mything-hello', ['name'], Container.hello)
