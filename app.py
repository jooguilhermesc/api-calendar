import os
from utils import workdays_calendar
from flask import Flask, Response, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/calendar', methods=['GET'])
def calendar():
    new_calendar = workdays_calendar().create_date_table()
    return Response(new_calendar.to_json(orient='table', date_format='iso'),mimetype='application/json')

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True)