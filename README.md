# Disaster Response Pipeline Project

## 1. Repository Structure:
```bash
├── app 
│   ├── templates├── go.html
│   └── run.py   └── master.html
├── data
│   ├── disaster_categories.csv
│   ├── disaster_messages.csv
│   └── process_data.py
├── images ├── message.png
│          ├── result1.png
│          ├── result2.png
│          ├── result3.png
│          ├── plot1.png
│          ├── plot2.png
├── models
│   └──train_classifier.py
└── README.md
```

## 2. Project Components

- ETL Pipeline <br>
process_data.py is a python script that make data cleaning pipeline:
  - Loads the messages and categories datasets
  - Merges the two datasets
  - Cleans the data
  - Stores it in a SQLite database

* ML Pipeline <br>
train_classifier.py is a python script that writes a machine learning pipeline:
  - Loads data from the SQLite database
  - Splits the dataset into training and test sets
  - Builds a text processing and machine learning pipeline
  - Trains and tunes a model using GridSearchCV
  - Outputs results on the test set
  - Exports the final model as a pickle file

* Flask Web App <br>
The files html and some part of run.py were already provided by Udacity's course. So my job on it, was:
  - Modify file paths for database and model as needed
  - Add data visualizations using Plotly in the web app. One example is provided.

## 3. Instructions:

* Run the following commands:
    - To run ETL pipeline that cleans data and stores in database <br>
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves <br>
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

* Run the following command in the app's directory to run your web app.
    `python run.py`

* Go to http://0.0.0.0:3001/


## 4. Project Motivation:

In this project, the goal is apply the skills learned on the lessons to analyze disaster data from Figure Eight to build a model for an API that classifies disaster messages.

The data set containing real messages that were sent during disaster events. I created a machine learning pipeline to categorize these events so that I can send the messages to an appropriate disaster relief agency.

My project includes a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data. 

## 5. App Demonstration

### Messages

![message](/images/message.png)



![result1](/images/result1.png)


![result2](/images/result2.png)


![result3](/images/result3.png)

### Plots 

![plot1](/images/plot1.png)


![plot2](/images/plot2.png)

