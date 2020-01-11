from dependencies import Injector
from mything.microfrontends.core import IHtml, webcomponent
import .CounterFrontend

 # __pragma__ ('js', '{}', 'IHtml = window.CustomHtml')

class Container(Injector):
  counter = CounterFrontend
  html = IHtml

webcomponent('mything-counter', ['page'], Container.counter)
