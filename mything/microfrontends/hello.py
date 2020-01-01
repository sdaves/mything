class Hello:
    def __init__(self):
        super().__init__()
        self.config = compose(
            withProps({'page': 'Home'}),
            withState('counter', 'setCounter', 0)
        )

    def render(self, props={'page':'Home', 'counter':0, 'setCounter':lambda x: None}):
        return h('div', {}, [
            props['page'], 
            props['counter'], 
            h('button', {'onClick': lambda: props['setCounter'](props['counter']+1)}, '+1')
        ])

    def mount(self, HTMLElement):
        mountPoint = document.createElement('span')
        self.attachShadow({ 'mode': 'open' }).appendChild(mountPoint)
        render(h(attach(self.config)(render), {'page': self.getAttribute('page')}), mountPoint)

if 'window' in globals(): window.defineElement('mything-hello', ['page'], lambda x: Hello().mount(x))
