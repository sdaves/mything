from mything.preact import h, compose, withProps, withState, attach

def Hello(props={'page':'Home', 'counter':0, 'setCounter':lambda: None}):
    return h('p', {}, page)

def HelloComposer(props={'page':'Home'}):
    return compose(
      withProps({'page': props['page']),
      withState('counter', 'setCounter', 0)
    )

def mount(self):
    mountPoint = document.createElement('span')
    self.attachShadow({ 'mode': 'open' }).appendChild(mountPoint)
    render(h(attach(HelloComposer())(Hello), {'page': self.getAttribute('page')}), mountPoint)

if 'window' in globals(): defineElement('mything-hello', ['page'], mount)
