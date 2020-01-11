from dependencies import Injector
from mything.microfrontends.core import IHtml, WebComponent
from mything.microfrontends.hello.HelloFrontend import HelloFrontend

 # __pragma__ ('js', '{}', 'IHtml = window.CustomHtml')

class Container(Injector):
    html = IHtml
    frontend = HelloFrontend
    component = WebComponent
    
Container.frontend # calls frontend constructor
