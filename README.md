# Insurance_Predictor
ML model to predict insurance premium based on certain features

The project entails analyzing a dataset provided by a leading insurance company and building a machine learning model to predict the insurance premium price based on certain features such as Age, Weight, AnyTransplants, NumberOfMajorSurgeries, etc.

# Key Insights from EDA and Hypothesis Testing
a. Premium price is found to be approximately normally distributed (visual inspection). Most insurance buyers pay between 22000 and 32000. The minimum premium paid is 14000, while the maximum is 40000.

b. Age is strongly positively correlated with premium price. Height and weight are weakly positively correlated with premium price.

c. Premium price, on average, increases as the number of surgeries increase. Also, older customers are found to have had more surgeries.

d. Premium price increases with presence of Diabetes, BloodPressureProblems, AnyTransplants, AnyChronicDiseases and HistoryOfCancerInFamily. While the price did not increase with the presence of KnownAllergies.

e. The premium price is found to vary with presence/increase of NumberOfMajorSurgeries.

# Model performance and conclusion
The model has an R2 score of 0.8764 and a MAPE value of 5.76%. So, the model has decent performance and can be used for predicting premium prices. This model will, on one hand, provide enhanced customization and reduced premiums to the customer, on the other hand it will help the insurance company in managing risks as now they will have premium values that will be fairly accurate thus help reducing the likelihood of non-performing assets (NPA). This will also help the insurance company in becoming more competitive.

# Model Deployment



