from flask import Flask, render_template, request
import pickle
import numpy as np


lasso_file = "lasso_reg.pkl" 
linear_file = "Linear_reg.pkl"
ridge_file = "ridge_reg.pkl"

lasso_reg = pickle.load(open(lasso_file,'rb'))
linear_reg = pickle.load(open(linear_file,'rb'))
ridge_reg = pickle.load(open(ridge_file,'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':
        
        batting_team = request.form['batting-team']
        bowling_team = request.form['bowling-team']
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        
        overs_runs_wickets_etc = [ runs, wickets,overs, runs_in_prev_5, wickets_in_prev_5]
        
        # batting team and bowling team
        bat_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        if batting_team =='Chennai Super Kings':
            bat_list[0] = 1
        elif batting_team == 'Delhi Daredevils':
            bat_list[1] = 1
        elif batting_team == 'Kings XI Punjab':
            bat_list[2] = 1
        elif batting_team == 'Kolkata Knight Riders':
            bat_list[3] = 1
        elif batting_team == 'Mumbai Indians':
            bat_list[4] = 1
        elif batting_team == 'Rajasthan Royals':
            bat_list[5] = 1
        elif batting_team == 'Royal Challengers Bangalore':
            bat_list[6] = 1    
        elif batting_team == 'Sunrisers Hyderabad':
            bat_list[7] = 1

        if bowling_team == 'Chennai Super Kings':
            bat_list[8] = 1
        elif bowling_team == 'Delhi Daredevils':
            bat_list[9] = 1
        elif bowling_team == 'Kings XI Punjab':
            bat_list[10] = 1
        elif bowling_team == 'Kolkata Knight Riders':
            bat_list[11] = 1
        elif bowling_team == 'Mumbai Indians':
            bat_list[12] = 1
        elif bowling_team == 'Rajasthan Royals':
            bat_list[13] = 1
        elif bowling_team == 'Royal Challengers Bangalore':
            bat_list[14] = 1    
        elif bowling_team == 'Sunrisers Hyderabad':
            bat_list[15] = 1 
        
        temp_array = bat_list + overs_runs_wickets_etc

        full_list = np.array([temp_array])        
        
        #my_prediction = int(regressor.predict(full_list)[0])

        
        prediction_1 = int( lasso_reg.predict(full_list) )
        prediction_2 = int(linear_reg.predict(full_list))
        prediction_3 = int(ridge_reg.predict(full_list))
        mean = int((prediction_1+prediction_2+prediction_3)/3)
        
        return render_template('result.html', prediction_1 = prediction_1, prediction_2 = prediction_2, prediction_3= prediction_3, mean= mean)
    
if __name__ == '__main__':
	app.run(debug=True)    