from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
        return "EVLİYİM VE KARİMA COK ASİGİM<33"
        
if __name__ == "__main__":
        app.run(debug =True)
   

        

