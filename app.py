from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/donationform')
def donationform():
    return render_template('donationform.html')

@app.route('/donationlist')
def donationlist():
    return render_template('donationlist.html')

if __name__ == '__main__':
  app.run(debug=True)
