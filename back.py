from flask import Flask, make_response, jsonify
from config import Config
from time import sleep
from newss import ne
from g_mail import auth_mail
from flask_cors import CORS


auth_mail()

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

@app.route("/api/<email>/<sus>")
def index(email: str, sus: str):

    print("pinged")

    sus = sus.replace(")", '/')
    ccc = ne([sus], email)
    


    try:
        res = make_response(jsonify({
        "View on government": ccc[0],
        "Department of government": ccc[1],
        "Parent company": ccc[2],
        "Author": ccc[3],
        "Date published": ccc[4],
        "Article link": sus
    }), 200)
    except:
        res = make_response(jsonify({
        "View on government": ccc[0],
        "Department of government": ccc[1],
        "Parent company": ccc[2],
        "Date published": ccc[3],
        "Article link": sus
    }), 200)
    
    return res

    

if __name__ == "__main__":
    app.run(debug=True)