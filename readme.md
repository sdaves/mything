# Mything

Pure Python Domain Driven Design microfrontends. Create standard wsgi microservices for your Domain, and HTML5 microfrontends by generating ES6!

## Badges

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/sdaves/mything)

## Requirements

- Install git `https://git-scm.com/downloads`
- Install Python 3.6 or greater and python3-venv `https://www.python.org/downloads/`

## Setup on Linux

    apt install -y git python3 python3-venv
    
## Setup on Mac

    brew install python3 git
    
## Setup on Windows10

    choco install python3 git

## Setup development tools (all platforms)

    git clone https://github.com/sdaves/mything
    cd mything
    python3 -m venv venv
    . venv/bin/activate
    
    # with system make
    make setup 
    
    # or
    
    # without system make
    python3 -m pip install --user py-make
    python3 -m pymake setup

## Build

    # with system make
    make 
    
    # or
    
    # without system make
    python3 -m pymake

## Test

    # with system make
    make test
    
    # or
    
    # without system make
    python3 -m pymake test

## Help

    # with system make
    make help
    
    # or
    
    # without system make
    python3 -m pymake help
