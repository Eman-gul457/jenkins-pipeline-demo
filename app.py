from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Jenkins CI/CD App</title>
            <style>
                body {
                    background: linear-gradient(135deg, #4facfe, #00f2fe);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                }
                h1 {
                    color: white;
                    font-size: 3em;
                    text-align: center;
                    text-shadow: 2px 2px 5px #333;
                }
                .box {
                    background: rgba(0,0,0,0.4);
                    padding: 20px 40px;
                    border-radius: 15px;
                }
            </style>
        </head>
        <body>
            <div class="box">
                <h1>🏗️ Jenkins CI/CD Pipeline Deployed Successfully!</h1>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
