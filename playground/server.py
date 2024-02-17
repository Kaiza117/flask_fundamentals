from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index1.html")

@app.route('/play/<x>')
def play2(x):
    times = int(x)
    return render_template("index2.html", times = times)    

@app.route('/play/<x>/<color>')
def play3(x,color):
    times = int(x)
    color = color
    return render_template("index3.html", times = times, color = color) 

if __name__ =="__main__":
    app.run(debug=True)   