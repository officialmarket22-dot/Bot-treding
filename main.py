from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot trading aktif ✅"

# contoh endpoint untuk bot (opsional)
@app.route("/signal")
def signal():
    return {"status": "OK", "signal": "BUY"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
