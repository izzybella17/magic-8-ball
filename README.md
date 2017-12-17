# magic-8-ball
Hello pals,
This program is for all my indecisive people out there who can't pick what to eat.
Basically it picks a random food place for you based on your location.

### Setting up API Keys
In order to get the app working on local machine you have to replace the value
of the API_KEY in the sample.cfg with your own Key. You'll also have to change the value
in the main.py file (default app_data.cfg).

### Prerequisites
Make sure to install all the prerequite packages from requirements.txt

##### Running the Flask Server
set the system variable FLASK_APP=server.py
```
export FLASK_APP=server.py
```
After setting that system variable, run the local server with
```
flask run
```

