from flask import Flask ,render_template


app= Flask(__name__)

@app.route('/<int:x>')
def play(x):
    return render_template("play.html",times=x)

if __name__=="__main__":
    app.run(debug=True)
    
   
