from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
        return "Evliyim ve karıma çok aşığım <3"
        
if __name__ == "__main__":
        app.run(debug =True)
   

        

