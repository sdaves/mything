from dependencies import Injector
from mything.microfrontends.core import IHtml, WebComponent
from mything.microfrontends.hello.CounterFrontend import CounterFrontend

 # __pragma__ ('js', '{}', 'IHtml = window.CustomHtml')

class Container(Injector):
    html = IHtml
    frontend = CounterFrontend
    component = WebComponent
    
Container.frontend # calls frontend constructor
