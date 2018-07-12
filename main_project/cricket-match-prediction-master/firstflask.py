from flask import Flask, request, url_for, redirect,render_template
from wtforms import Form, TextAreaField, validators
import cgi
import cgitb
import modelGenerator
import graph

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
            print(select)
            player=str(request.form.get('searchplayer'))
            print(player)
            graph.graphofplayer(select,player)
            return render_template('UI1.html')

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

@app.route('/player_XI', methods=['GET', 'POST'])
def player_XI():
    if request.method == 'POST':
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