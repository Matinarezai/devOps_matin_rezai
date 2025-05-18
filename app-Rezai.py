from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
<<<<<<< HEAD
    return "Salut, ALED WTF DEVOPS NANI,text vite , test pour le doc "
=======
    return "Bienvunue au Flask, ce site est pour tester zakir haidari"
>>>>>>> e34cccf1de71ffe67293af52c78ccf8af4912529

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

