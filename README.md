#🏠 Bangalore House Price Prediction – ML Web Application
## 📌 Overview

A production-style Machine Learning web application that predicts Bangalore house prices based on user inputs such as location, total square feet, number of bathrooms, and BHK configuration.
The application is built using:
FastAPI for the backend prediction API
Streamlit for the interactive frontend
Linear Regression as the final trained model
AWS EC2 for cloud deployment

This project demonstrates full-stack ML deployment including model training, API development, frontend integration, and cloud hosting.

---

##🚀 Live Demo

###🌐 Public URL:
  http://ec2-16-170-159-229.eu-north-1.compute.amazonaws.com/
  
---

##🏗 System Architecture
-User → Streamlit UI → FastAPI Backend → Trained ML Model → Price Prediction → UI Display
-The frontend collects user inputs
-Sends request to FastAPI backend
-Backend loads trained model
-Model predicts house price
-Result displayed dynamically on UI

---

## 🔧 Tech Stack

| Tech         | 			Purpose                     |
|--------------|----------------------------------------|
| Python       | Core backend & ML development          |
| Pandas       | Data cleaning & preprocessing          |
| NumPy        | Numerical computations             	|
| Scikit-learn | Model training & hyperparameter tuning |
| Matplotlib   | Plotting & visualization         		|
| FastAPI      | Backend REST API for predictions 		|
| Uvicorn      | ASGI server for running FastAPI  		|
| Streamlit    | Interactive frontend user interface  	|
| AWS EC2      | Cloud hosting & deployment          	|
| systemd      | Service management on Ubuntu server 	|
| git          | Version Control           	         	|
| github       | Code hosting					     	|

---

## 📊 Model Details
###🔹 Algorithms Tested
Linear Regression
Lasso Regression
Decision Tree Regressor

###🔹 Hyperparameter Tuning

Performed using GridSearchCV with ShuffleSplit cross-validation.

###🔹 Final Model Selected

Linear Regression
Best R² Score (Test Set): 0.845
Best Parameter: fit_intercept=True

The model achieved strong generalization performance after feature engineering and tuning.

---

## 🚀 How to Run This Project

1. **Clone this repository**
   ```bash
   git clone https://github.com/Kelvinjohnson5249/Banglore_House_Price_Prediction
   ```
   
2.  **Navigate into the folder**
	```bash
	cd Banglore_House_Price_Prediction
	```

3.  **Create Virtual Environment**
	```bash
	python -m venv venv
	venv\scripts\activate
	```
4. **Install Dependencies**
	```bash
	pip install -r requirements.txt
	```
5. **Run Backend**
	```bash
	uvicorn Server.main:app --reload
	```
6. **Run Frontent**
	```bash
	streamlit run Client/app.py
	```
---

## Deployment Details
Hosted on AWS EC2 (Ubuntu 22.04)

Backend served using Uvicorn

Frontend served using Streamlit

Publicly accessible via EC2 DNS

##👤 Author

Kelvin Johnson
📧 kevinjohnson5249@gmail.com
📍 New Delhi, India

## ⭐ Feedback & Contributions

Feel free to suggest improvements or open issues.  
If you found this project helpful, don’t forget to ⭐ the repository on GitHub!
