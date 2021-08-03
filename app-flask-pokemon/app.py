from flask import Flask, render_template, request

app = Flask(__name__)

# url router
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/evolution")
def evolution():
    return render_template("evolution.html")


# api
@app.route("/evo",methods=['GET','POST'])
def evo():
    dataFromWeb = request.form

    print("--pokemon--")
    print(dataFromWeb["pokemon"])
    print("--stone--")
    print(dataFromWeb["stone"])
    print("-----")

    if(dataFromWeb["pokemon"] == "皮卡丘" and dataFromWeb["stone"] == "雷之石"):
        response = {"evoPokemon": "雷丘"}
    else:
        response = {"evoPokemon": "無法進化"}

    return response

if __name__ == "__main__":
    app.run(host="localhost", port="5000", debug=True)