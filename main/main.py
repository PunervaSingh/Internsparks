keyid = 'rzp_test_72b14Bb260520s'
keysecret = 'BpIsSYWreMjd2bN4BRKamo5Q'

from flask import Flask, render_template, request, redirect, session, url_for, flash
import razorpay
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
razorpay_client = razorpay.Client(auth=(keyid, keysecret))
ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///internship.db'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://volhmwzchxljyz:d600c60f51b6b8148ab697d2e02c98c9b93cfc4f2ac74373c5c342f62800447c@ec2-34-233-187-36.compute-1.amazonaws.com:5432/dbltiienqrsb2k'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    mobile = db.Column(db.String(20))
    msg = db.Column(db.Text())

    def __init__(self, name, email, mobile, msg):
        self.name = name
        self.email = email
        self.modile = mobile
        self.msg = msg

@app.errorhandler(500)
def internal_error(error):
    flash('Facing Internal server error. Try again later...', "success")
    return render_template('home.html'),500

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('home.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        msg = request.form['msg']
        # print(name, dealer, msg)
        if name == '' or email == '':
            return render_template('contact.html', message='Please enter required field')
        data = Contact(name, email, mobile, msg)
        db.session.add(data)
        db.session.commit()
        flash('Your message has been sent successfully...', "success")
        return render_template('home.html')
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/guide')
def guide():
    return render_template('guide.html')

# if __name__ == '__main__':
#     app.secret_key = 'super secret key'
#     app.run(debug=True)