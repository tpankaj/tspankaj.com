import datetime
from flask import *
app = Flask(__name__)

@app.context_processor
def get_date():
    return dict(year=datetime.datetime.today().year)

# THIS IS TEMPORARY
@app.context_processor
def get_projects():
    return dict(projects=[{"name": "FRC Computer Vision", "url": "frc-computer-vision"}])

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/projects/')
def projects():
    return render_template('projects.html')

@app.route('/projects/frc-computer-vision/')
def project_page():
    return render_template('frc-computer-vision.html')

@app.route('/robots.txt')
def robots_txt():
    return app.send_static_file('robots.txt')

@app.route('/humans.txt')
def humans_txt():
    return app.send_static_file('humans.txt')

if __name__ == '__main__':
    app.run(debug=False)
