
from traceback import print_stack
from flask import Flask, render_template, request,redirect,url_for
import csv

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/donationform', methods=['GET','POST'])
def donationform():
    if request.method == 'GET':
        return render_template('donationform.html')
    elif request.method == 'POST':
        b=request.form['name']
        g=request.form['email']
        A=request.form['number']
        h=request.form['book name']
        x=request.form['address']
        book=(b,g,A,h,x)
        n= open('data.csv', 'a', newline='')
        j= csv.writer(n)
        j.writerow(book)
        n.close()


        return render_template('donationform.html')


@app.route('/donationlist')
def donationlist():
    l=open('data.csv', 'r')
    k=csv.reader(l)
    books=[]
    try:
        for bookdata in k:
            book={
                'name':bookdata[0],
                'email': bookdata[1],
                'number': bookdata[2],
                'book': bookdata[3],
                'address': bookdata[4],
            }
            books.append(book)
    except:
        return render_template('donationlist.html')

    return render_template('donationlist.html',bookslist=books)

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
            return render_template('login.html', error='Incorrect username or password')


if __name__ == '__main__':
  app.run(debug=True)
