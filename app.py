from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/index.html')
def my_home():
    return render_template('./index.html')


def write_to_file(data):
    with open('database.txt', "a") as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open('database.csv', "a", newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/<string:pagename>')
def htmlpage(pagename):
    return render_template(pagename)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return "something went wrong"
    else:
        return 'something went wrong'
