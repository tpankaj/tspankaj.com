import json
import datetime
import flask
app = flask.Flask(__name__)

@app.route('/')
def root():
    #projects = json.load(open('json/projects.json', 'r'))
    #return flask.render_template('index.html', projects=projects, year=datetime.datetime.today().year)
    return 'Hello, world!'

@app.route('/projects/')
def projects():
    projects = json.load(open('json/projects.json', 'r'))
    return flask.render_template('projects.html', projects=projects, year=datetime.datetime.today().year)

@app.route('/projects/frc-targeting/')
def project_page():
    projects = json.load(open('json/projects.json', 'r'))
    return flask.render_template('frc-targeting.html', projects=projects, year=datetime.datetime.today().year)

@app.route('/robots.txt')
def robots_txt():
    return app.send_static_file('robots.txt')

@app.route('/humans.txt')
def humans_txt():
    return app.send_static_file('humans.txt')

if __name__ == '__main__':
    app.run(debug=True)
