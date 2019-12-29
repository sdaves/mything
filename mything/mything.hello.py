from standalone.module import Component, h, render

class Hello(Component):
    def __init___(self):
        super().__init__()
        self.display = 'Hello'

    def render(self):
        return h('p', {}, self.display)
    
element = h(Hello, {'name': 'React!'})
render(element, 'container')
