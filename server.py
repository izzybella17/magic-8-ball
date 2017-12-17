from flask import Flask
import main

#Startin Flask App
app = Flask(__name__)

@app.route("/")
def index():
    #If the program works properly you should see a restaurant from anaheim
    business = main.getRandomBusiness(main.DEFAULT_TERM, main.DEFAULT_LOCATION)
    return business['name']

