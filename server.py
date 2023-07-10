import os
import csv
from flask import Flask, render_template, send_from_directory, url_for, request, redirect

app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<page_name>')
def html_page(page_name):
    return render_template(page_name)

# def write_file(data):
#     with open('db.txt', mode='a') as db:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = db.write(f'\n{email},{subject},{message}')

def write_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    # return 'Form Submitted, Yess Dooonk'
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try Again!'

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/index.html')
# def my_home():
#     return render_template('index.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/contact.html')
# def kontak():
#     return render_template('contact.html')

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico')