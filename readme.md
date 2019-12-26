# Mything

Pure Python Domain Driven Design microfrontends. Create standard wsgi microservices for your Domain, and HTML5 microfrontends by generating ES6!

## Badges

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/sdaves/mything)

## Requirements

- Install git `https://git-scm.com/downloads`
- Install Python 3.7.6 or greater with pip included `https://www.python.org/downloads/`

## Setup on Linux

    apt install -y git python3-venv python3-openssl python3-setuptools python3-pip 
    
## Setup on Mac

    brew install python3 git
    
## Setup on Windows10

    choco install python3 git

## Setup development tools (all platforms)

    git clone https://github.com/sdaves/mything
    cd mything
    python3 -m pip install --user setuptools py-make poetry
    python3 -m pymake setup

## Build, Docs, Test

    python3 -m pymake

## Help

    python3 -m pymake help
