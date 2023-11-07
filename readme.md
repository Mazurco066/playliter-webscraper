# Description

Webscrapper module for playliter api.

## Setup

Virtual env setup:

```sh
# if you do not have your virtual env created just create one
python3 -m venv .venv

# Activate virtual env
source .venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# If you want do deactivate virtual env
deactivate

# if you change any of the dependencies update it running
pip freeze > requirements.txt
```

Api setup:

```sh
# Run the api using this command
uvicorn main:app --reload
```

## Author

* [@Mazurco066](https://github.com/Mazurco066).