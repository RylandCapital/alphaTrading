AlphaDefi Trading Systems

This repo is built on top/using https://github.com/ccxt/ccxt

AlphaDefi Trading Systems is set up for Kucoin but you can change to whatever you like you would just need to edit config files with new env variables.

# Install instructions 
- Create a new virtualenv
  - Make sure `python3 --version`
  - `pip install virtualenv` if not already installed
  - `python3 -m venv {PROJECT NAME}`
- Run `source env/bin/activate`
- Install the packages using `pip install -r requirements.txt` 

# Before running code 
- Run `source env/bin/activate`

# add .env file with api keys and secrets 
- see config file for needed env vars

# When making changes in packages
- Run `pip install XX`
- Run `pip freeze > requirements.txt` 

# Compile and run docker
- Compile docker: `docker build -t alpha-trading-systems .`
- Run docker `docker run -t alpha-trading-systems`