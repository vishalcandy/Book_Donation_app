from flask import Flask, render_template, request,redirect

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/donationform', methods=['GET','POST'])
def donationform():
    if request.method == 'GET':
        return render_template('donationform.html')
    elif request.method == 'POST':
        g=request.form['email']
        A=request.form['number']
        h=request.form['book name']
        x=request.form['address']
        book={
            'email': g,
            'number': A,
            'book' : h,
            'address': x
        } 
        print (book)

        return render_template('donationform.html')


@app.route('/donationlist')
def donationlist():
    return render_template('donationlist.html')

e='admin username' 
f='admin password'
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        d=request.form['username']
        c=request.form['password']
        if d == e and c == f:
           return redirect('/donationlist')

        else: 
            return render_template('login.html')


if __name__ == '__main__':
  app.run(debug=True)
