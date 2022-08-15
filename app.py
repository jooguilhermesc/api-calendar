import os
from datetime import datetime
from utils import workdays_calendar
from flask import request, Flask, Response, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
@app.route('/calendar/', methods=['GET','POST'])
def calendar():
    start = '2010-01-01'
    end = datetime.today().strftime('%Y-%m-%d')
    dt_start = start if request.args.get("dt_start") is None else request.args.get("dt_start")
    dt_end = end if request.args.get("dt_end") is None else request.args.get("dt_end")
    new_calendar = workdays_calendar(start=dt_start,end=dt_end).create_date_table()
    return Response(new_calendar.to_json(orient='table', date_format='iso' ,force_ascii=False),mimetype='application/json')

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True)