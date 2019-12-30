from mything.preact import h, compose, withProps, withState, attach

def Hello(props={'page':'Home', 'counter':0, 'setCounter':lambda: None}):
    return h('div', {}, [
        props['page'], 
        props['counter'], 
        h('button', {'onClick': props['setCounter']}, '+1')
    ])

P = compose(
    withProps({'page': 'Home'}),
    withState('counter', 'setCounter', 0)
)

def mount(self):
    mountPoint = document.createElement('span')
    self.attachShadow({ 'mode': 'open' }).appendChild(mountPoint)
    render(h(attach(P)(Hello), {'page': self.getAttribute('page')}), mountPoint)

if 'window' in globals(): defineElement('mything-hello', ['page'], mount)
