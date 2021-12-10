from flask import Flask, jsonify
from flask_restful import Api, Resource
import pickle
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, RobustScaler
from flask_cors import CORS, cross_origin


app = Flask(__name__)
api = Api(app)


class predictInvestment(Resource):
  @cross_origin()
  def get(self, i_price, i_zestimate, i_rent_zestimate, i_zipcode):
    # print( price + ' '+ zestimate)
    price = float(i_price)
    zestimate = float(i_zestimate)
    rent_zestimate = float(i_rent_zestimate)
    zipcode = i_zipcode
   
    df = pd.read_csv('final_house_data.csv')
   
    downpayment = zestimate * 0.2
    loanAmount = zestimate - downpayment
    interest = loanAmount *.03
    loanAmount = loanAmount + interest
    mortgage_calculated = loanAmount/30 
    
    # HOA
    hoa = np.random.randint(350, 550, size=1)
    rental_income =rent_zestimate-(mortgage_calculated + hoa)
   
    Change= np.random.randint(5,8, size=1)
    

    time_elasped = np.random.randint(50, 500, size=1)
   

    increase_in_neighbourhood= np.random.randint(2,9, size=1)
    # house_data['increase_in_neighbourhood']= increase_in_neighbourhood * 1

   
    
    testcondition = "Zip_code == {0}".format(zipcode)
   
    test_df = df.query(testcondition)
    if test_df.empty:
      print('if')
      temp_prop_crime = 0
      temp_v_crime = 0
      temp_commute_time = 0
    else:
      temp_prop_crime =  test_df.iloc[0].Property_Crime
      temp_v_crime = test_df.iloc[0].Violent_crime
      temp_commute_time = test_df.iloc[0].commute_time
     
  
    
    input_list =[[price, rental_income, Change, time_elasped + 1000, increase_in_neighbourhood, temp_prop_crime, temp_v_crime, temp_commute_time],
                [price, rental_income, Change, time_elasped + 1000, increase_in_neighbourhood, temp_prop_crime, temp_v_crime, temp_commute_time]]
    house_data = pd.DataFrame(input_list, columns = ['Price','RentalIncome','Change %','time_elasped_after2years','increase_in_neighbourhood', 'Property_Crime','Violent_crime','commute_time'])
    house_data.fillna(0.0, inplace=True)
    
    # X_test  = pd.DataFrame()
    file = open('AdaBoostModel', 'rb')
    clf = pickle.load(file)
    y_pred = clf.predict(house_data[0:2])
   
    # body = 'Not a good investment !'
    response =  jsonify(message="Good investment !")
    # return {"data" : "Not a Good investment !"}
    if y_pred[0] == 0:
      # body = 'Good investment !'
      response =  jsonify(message="Not a Good investment !")
    
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# api.add_resource(predictInvestment, "/predictInvestment/<float:price>/<float:zestimate>/<float:rent_zestimate>/<string:zipcode>")
api.add_resource(predictInvestment, "/predictInvestment/<string:i_price>/<string:i_zestimate>/<string:i_rent_zestimate>/<string:i_zipcode>")

if __name__ == "__main__":
  app.run(debug = True)



