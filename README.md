# Fraud-Detection-web-service

Serving a machine learning model as a webservice using Python, Flask, Docker, AWS ec2.\
I have used Credit Card Fraud Detection from kaggle link below\
https://www.kaggle.com/mlg-ulb/creditcardfraud

# Getting Started
1.Run python fraud_detection.py to generate pkl file this is the format where your machine learning model is saved as object.\
2.Use app.py to wrap the inference logic in a flask server to serve the model as a REST webservice\
3.Execute the command python app.py to run the flask app.\
4.Go to the browser and hit the url 0.0.0.0:80 to get a message Hello World! displayed. You can change the port according to your availability\
5.Next, run the below command in terminal to query the flask server\
&nbsp;&nbsp;Run docker build -t deploy-model . to build the docker image using Dockerfile.\
&nbsp;&nbsp;Run docker run -p 80:80 deploy-model to run the docker container that got generated using the deploy-model docker image. (This assumes that the port in app.py is set to 80)
