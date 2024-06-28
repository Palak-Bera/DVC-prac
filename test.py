import pandas as pd 


Data = [
    
    
    {"name": "Palak" , "age" : 22 , " city" : "Dubai"},
    {"name": "Priyank" , "age" : 27 , " city" : "London"},
    {"name": "Darshit" , "age" : 30 , " city" : "Ahmedabad"},
    {"name": "Virat" , "age" : 45  , " city" : "Delhi"},
    {"name": "Rohit" , "age" : 47 , " city" : "Mumbai"},
    {"name": "Dhoni" , "age" : 53 , " city" : "Ranchi"},
]



Data =  pd.DataFrame(Data)

Data.to_csv("data/data.csv", index =  False)