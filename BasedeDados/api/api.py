from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about', methods = ['get'])
def about():
    return 'About'
if __name__ == '__main__':
    print("Starting Flask server...")
    


    print("quero ir tomar banho")
    app.run(debug=False)


   
