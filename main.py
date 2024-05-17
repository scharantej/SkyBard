
# Import necessary modules
from flask import Flask, render_template, request
from sonnets import generate_sonnet

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/sonnet', methods=['POST'])
def sonnet():
    flight_number = request.form['flight_number']
    date = request.form['date']
    sonnet = generate_sonnet(flight_number, date)
    return render_template('sonnet.html', sonnet=sonnet)

if __name__ == '__main__':
    app.run(debug=True)
