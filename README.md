Virtual Env Set Up On Mac

go into a new directory and `run python3 -m venv env`

Open the new virtual environment by running `source env/bin/activate`

Install dependencies with `pip install -r requirements.txt`

Start the UI up with `python manage.py runserver` and go to localhost:8080

## How to run tests

inside your vritual env, navigate to your tests directory and run `make test` for unit tests on the helper functions, or `make slowtest` for an end-to-end test.
