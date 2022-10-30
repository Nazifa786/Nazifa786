from flask import Flask

app = Flask(__name__)

if(__name__=="__main__"):
    app.run()
    
@app.route("/")
def welcome() :
    return "Welcome to Python Web Services"
