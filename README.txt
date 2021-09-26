Identify Cyber Attack events

This project contains the solution to a problem of identifying cyber attacks given 10 variables as input.
It is an anomally detection problem.

In this folder the following files are included:
-Anomaly_detection_case.ipynb:  contains the code used for the solution with all the explanations along the way.
-data.csv: Contains the data for the case. 30k cyber events with 32 known flagged as anomalies. For the rest the status is unknown.
-finalized_model.pkl:  The saved model
-app.py: A flask api to deploy the app locally. Execute it as a script ( >python app.py) from a terminal and then access localhost:5000 or similar in a browser.
	You can input the 10 variable values, hit predict and a prediction will be made by the model if it is an anomaly or not.
-Report Anomaly Detection.docx:  A report containing the explanation of the steps followed to tackle the case.
-templates: Contains an index.html file for the front-end of the app.