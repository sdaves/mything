from .proppy import h, compose, withProps, withState, attach

def render(props={'page':'Home', 'counter':0, 'setCounter':lambda x: None}):
    return h('div', {}, [
        props['page'], 
        props['counter'], 
        h('button', {'onClick': lambda: props['setCounter'](props['counter']+1)}, '+1')
    ])

config = compose(
    withProps({'page': 'Home'}),
    withState('counter', 'setCounter', 0)
)

def mount(self):
    mountPoint = document.createElement('span')
    self.attachShadow({ 'mode': 'open' }).appendChild(mountPoint)
    render(h(attach(config)(render), {'page': self.getAttribute('page')}), mountPoint)

if 'window' in globals(): window.defineElement('mything-hello', ['page'], mount)
