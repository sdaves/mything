# Mything

Pure Python Domain Driven Design. Create standard wsgi microservices for your Domain, and HTML5 microfrontends by generating ES6!

## Requirements

- Install Python 3.7.6 or greater with pip included `https://www.python.org/downloads/`
- Install git `https://git-scm.com/downloads`

## Setup on Linux

    apt install -y python3-pip git
    
## Setup on Mac

    brew install python3 git
    
## Setup on Windows10

    choco install python3 git

## Setup development tools (all platforms)

    git clone https://github.com/sdaves/mything
    cd mything
    python -m pip install py-make poetry
    python -m pymake setup

## Build, Docs, Test

    python -m pymake

## Help

    python -m pymake help
