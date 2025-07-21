from flask import Flask, render_template

application = Flask(_name_)

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/contact')
def contact():
    return render_template('contact.html')

@application.route('/project')
def project():
    return render_template('project.html')

if _name_ == '_main_':
    application.run()