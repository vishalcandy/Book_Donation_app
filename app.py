from flask import Flask, render_template, request,redirect,url_for,send_from_directory
import csv

app = Flask(__name__)

@app.route('/')
def homepage():
    l=open('data.csv', 'r')
    k=csv.reader(l)
    bookdata=[]
    try:
        for currentbook in k:
            book={
                'name':currentbook[0],
                'email': currentbook[1],
                'number': currentbook[2],
                'book': currentbook[3],
                'address': currentbook[4],
            }
            bookdata.append(book)
    except:
        return render_template('donationlist.html')
    l.close()
    totalBooks = {}
    print(bookdata)
    for book in bookdata:
        try:
            useremail = book['email']
            currentBookCount = totalBooks[useremail]
            totalBooks[useremail] = currentBookCount + 1
        except:
            useremail = book['email']
            totalBooks[useremail] = 1

   

    for book in bookdata:
        try:
            useremail = book['email']
            username = book['name']
            totalBookCount = totalBooks[useremail]
            totalBooks[username] = totalBookCount
            del totalBooks[useremail]
        except:
            continue


   
    marklist = sorted(totalBooks.items(), key=lambda x:x[1])
    sortdict = dict(marklist)
    totalBooksInAscOrder = list(sortdict.items())

  
    topDonorsList = []
    for item in totalBooksInAscOrder:
        topDonorsList.insert(0, item)

    

    
    return render_template('home.html',topdonorslist=topDonorsList)

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
    l.close()

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


@app.route('/sw.js')
def sw():
    return send_from_directory('static', 'sw.js')

@app.route('/aboutme')
def aboutme():
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
        return render_template('aboutme.html')
    l.close()

    return render_template('aboutme.html',bookslist=books)

e='admin username' 
f='admin password'

@app.route('/topdonors')
def topdonors():
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
        return render_template('topdonors.html')
    l.close()

    return render_template('topdonors.html',bookslist=books)

e='admin username' 
f='admin password'



    

#if __name__ == '__main__':
  #app.run(debug=True,Host='192.168.3.11')
 
if __name__ == '__main__':
  app.run(debug=True)

