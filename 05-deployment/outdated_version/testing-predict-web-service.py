#!/usr/bin/env python
# coding: utf-8



import requests


url = 'http://127.0.0.1:9696/predict'


customer = {
  "gender": "female",
  "seniorcitizen": 0,
  "partner": "yes",
  "dependents": "no",
  "tenure": 1,
  "phoneservice": "no",
  "multiplelines": "no_phone_service",
  "internetservice": "dsl",
  "onlinesecurity": "no",
  "onlinebackup": "yes",
  "deviceprotection": "no",
  "techsupport": "no",
  "streamingtv": "no",
  "streamingmovies": "no",
  "contract": "month-to-month",
  "paperlessbilling": "yes",
  "paymentmethod": "electronic_check",
  "monthlycharges": 29.85,
  "totalcharges": 29.85
}




response = requests.post(url, json=customer)


print(response.json())


if response[churn] == True:
    print("The customer will churn.")
else:
    print("The customer will not churn.") 


