from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>hello world<h1>"
@app.route("/dojo")
def coding():
    return "<h1>Dojo</h1>"
@app.route('/say/<name>')
def say(name):
    return "Hi " + name
@app.route("/repeat/<count>/<last>")
def printer(count,last):
    new = ""
    for i in range(int(count)):
        new += last      
    return new  
if __name__ =="__main__":
    app.run(debug=True)   