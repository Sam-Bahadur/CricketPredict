from flask import Flask, request, url_for, redirect,render_template
from wtforms import Form, TextAreaField, validators
import cgi
import cgitb
import modelGenerator
import graph
import database

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('UI1.html')

@app.route('/UI1', methods=['GET', 'POST'])
def UI1():
    if request.method == 'POST':
        if str(request.form.get('Result Prediction'))=='Result Prediction':
            return render_template('UI2.html')
        elif str(request.form.get('search'))=='search':
            select=str(request.form.get('select'))
            #print(select)
            player=str(request.form.get('searchplayer'))

            #print(player)
            graph.graphofplayer(select,player)
            a,b,c,d,e,f=database.readdata(player)
            #a1= ", ".join( repr(e) for e in a )
            a1=str(a)[2:-3]
            b1=str(b)[2:-3]
            c1=str(c)[2:-3]
            d1=str(d)[2:-3]
            e1=str(e)[2:-3]
            f1=str(f)[2:-3]

            return render_template('UI4.html',naam=player,m=a1,i=b1,r=c1,h=d1,avg=e1,sr=f1)


        else:
            return redirect(url_for('UI1'))

    elif request.method=='GET':
        return "sorry"



@app.route('/UI2', methods=['POST'])
def UI2():
    teamA =str(request.form.get('team1')).title()
    teamB=str(request.form.get('team2')).title()
    venue=str(request.form.get('venue')).capitalize()
    tosswin=str(request.form.get('tosswin')).title()
    dec=str(request.form.get('tossdis'))
    a,b,c,d = modelGenerator.startPrediction(teamA, teamB, venue, tosswin, dec)
    return render_template('UI3.html',value=a,value1=b,value2=c,value3=d)
    #return render_template('welcome.php')

@app.route('/UI4', methods=['GET', 'POST'])
def UI4():
    if request.method == 'POST':
        a=UI1()

        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return 'her'

   # show the form, it wasn't submitted
    return "helll"

#@app.route('/CapstoneProject/')
#def CapstoneProject():
  #print 'I got clicked!'

 # return render_template('CapstoneProject.py')

if __name__=='__main__':
    app.run(debug=True)