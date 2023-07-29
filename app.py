from flask import Flask, render_template, request

app = Flask(__name__)

#created a global dictionary
REGISTRANTS = {}
#created a global list 
SPORTS = [
    "Basketball",
    "Soccer",
    "ulitmate Frisbee"
]

#this function is tthe defualt page of website
@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

#this fucntion handles all registration for a sport
@app.route("/register", methods=["POST"]) #"POST" is being used because data is being recieved from a form
def resgister():
    name = request.form.get("name") #using request.form.get() is how to get "name" data from form
    #ATTENTION: MUST always do Server-side validation
    if not name: #if no name is provided in form.... 
        return render_template("failure.html") #... go to failure.html
    sport = request.form.get("sport") #getting "sport" data from form using request.form.get() 
    if sport not in SPORTS: #if sport cant be found...
       return render_template("failure.html") #... go to failure.html
    #assigning values to global dictionary...
    REGISTRANTS[name] = sport #used "name" as key and "sport" as value. KEY:name, VALUE:sport
    return render_template("success.html")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)



if __name__ == "__main__":
    app.run(debug=True)
