AlphaDefi Trading Systems

This repo is built on top/using https://github.com/ccxt/ccxt

AlphaDefi Trading Systems is set up for Kucoin but you can change to whatever you like.

# Install instructions 
- Create a new virtualenv
  - Make sure `python3 --version` returns 3.9.4
  - `pip install virtualenv`
  - `python3 -m venv env`
- Run `source env/bin/activate`
- Install the packages using `pip install -r requirements.txt` 

# Before running code 
- Run `source env/bin/activate`

# When making changes in packages
- Run `pip install XX`
- Run `pip freeze > requirements.txt` 

# Compile and run docker
- Compile docker: `docker build -t alpha-trading-systems .`
- Run docker `docker run -t alpha-trading-systems`