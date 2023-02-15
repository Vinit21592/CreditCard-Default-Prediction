# Credit-Card-Default-Prediction

![CCD](https://user-images.githubusercontent.com/78821357/218680447-82cf98f8-b480-4219-955f-2c7446bf3eb4.jpg)


### Problem Statement
Financial threats are displaying a trend in the credit risk of commercial banks as the incredible improvement in the financial industry has arisen. In this way, one of the biggest threats faced by commercial banks is the risk prediction of credit clients. The goal is to predict the probability of credit default based on the credit card owner's characteristics and payment history.

### Solution Proposed
There are two solutions here, the first is developing a web-based API interface for us to predict whether customer will default next month or not based on the details of the customer and the second approach is using batch prediction in which a csv file containing all the customer details will be taken as batch input and will generate a prediction file for each customer as an output.

### Dataset
The dataset is in .csv format and the data was collected from the source link below.
Data Source: https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset

### Tech Stack Used
1. Python
2. VS Code
3. Jupyter Notebook
4. Machine Learning Algorithms
5. Docker
6. MongoDB

### Infrastructure Required
1. AWS EC2
2. AWS ECR
3. AWS S3
4. GitHub Actions
5. Apache Airflow

### Approach
Performed various machine learning tasks like Data Pre-processing, Data Visualization, Feature Engineering, Model Building, Model Testing etc. to build a solution that should be able to predict the probability of whether a customer becomes a defaulter or not.

The following approach explains the project lifecycle :
  * **Data Preprocessing** : Exploring the data using pandas, numpy & identifying null values, missing values and outliers present in the dataset.
  * **Data Visualization** : Visualize the data through matplotlib, seaborn for finding insights of the variables present the dataset.
  * **Feature Engineering** : Cleaning the data to select and transform the most relevant variables from raw data.
  * **Model Building** : For model building we split the data into train and test. Then we train our model on different ML classification algorithms like :
     1. Gradient Boosting
     2. AdaBoost
     3. XGBoost
     4. Decision Tree
     5. Random Forest
     6. Logistic Regression
  * **Model Testing** : We use test data to get the predicted values and the model with best accuracy_score is selected. The best model is saved for predictions.
  * **Tuning** : Performed Hyperparameter tuning using RandomizedSearchCV and GridSearchCV to get the best parameters.
  * **Webpage** : We use apache airflow for pipeline training and for batch predictions.
  * **Deployment** : The project is deployed on AWS using airflow.
  
### Deployment Link
  
```bash
http://ec2-65-0-21-196.ap-south-1.compute.amazonaws.com:8080
```
  
### Web Interface
* **Airflow Login page**
  
To access Airflow, user will need to sign in using username and password as shown in the login page below.
![Airflow login page](https://user-images.githubusercontent.com/78821357/218680245-7a18d011-2793-4493-ad77-565032b1de90.png)
  
* **DAGs (directed acyclic graph) homepage**
  
After login user will get list of DAGs, out of which user can select creditcard_training to retrain the training pipeline if required or batch_prediction to make  batch predictions.
![Airflow - Dags](https://user-images.githubusercontent.com/78821357/218697454-fb7e0609-8275-4525-969c-f87134025a0d.png)

* **Creditcard_training homepage**

After selecting creditcard_training DAG user is directed to this page where user can train the pipeline manually or can see training pipeline schedule like next run or when is the next training schedule. The Schedule:@weekly will automatically start retraining on weekly basis so that triggering pipeline manually is not required. User can also access training log status of each run.
![Airflow - training-Graph](https://user-images.githubusercontent.com/78821357/218699066-a88c05e6-598a-4388-be05-9711b0bc94b4.png)

* **Batch_prediction homepage**

Similar to training DAG user can access batch_prediction DAG. For batch predictions user has to upload csv file in input_files folder in S3 bucket and then user can trigger batch prediction manually or else it will run as per scheduled. After making predictions the prediction file will get uploaded in prediction_files folder in S3 bucket.
![Airflow-batch-prediction-graph](https://user-images.githubusercontent.com/78821357/218699587-3a8040ce-c9ad-4c7c-8a5f-926f537a486f.png)


### How to run?
Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances.

### Data Collections
![Data Collection](https://user-images.githubusercontent.com/78821357/218706207-7d4235a2-a448-4049-ad26-01fc543a1366.png)

### Project Training Pipeline
![Training Pipeline](https://user-images.githubusercontent.com/78821357/218709407-48f0e28e-dfd1-43e1-8de8-2dbde3cc07ac.png)

### Deployment Architecture
![Deployment Architecture](https://user-images.githubusercontent.com/78821357/218709683-5db71a6f-9b77-42d2-9320-bd8530138268.png)

#### Step 1: Clone the repository
```bash
git clone https://github.com/Vinit21592/CreditCard-Default-Prediction.git
```

#### Step 2- Create a conda environment after opening the repository
```bash
conda create -n creditcard python=3.8 -y
```
```bash
conda activate creditcard
```

#### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

#### Step 4 - Export the environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

export MONGODB_URL="mongodb+srv://<username>:<password>@cluster0.dl9uoq9.mongodb.net/?retryWrites=true&w=majority"
```

#### Step 5 - Run the application server
```bash
python main.py
```
```bash
python train.py
```

### Run locally
1. Check if the Dockerfile is available in the project directory

2. Build the Docker image
```bash
docker build --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> --build-arg AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> --build-arg AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION> --build-arg MONGODB_URL=<MONGODB_URL> . 
```
3. Run the Docker image
```bash
docker run -d -p 8080:8080 <IMAGE_NAME>
```

To run the project first execute the below commmand. MONGO DB URL:
```bash
mongodb+srv://Vinit21592:vins21592@cluster0.dl9uoq9.mongodb.net/?retryWrites=true&w=majority
```
windows user
```bash
MONGO_DB_URL=mongodb+srv://Vinit21592:vins21592@cluster0.dl9uoq9.mongodb.net/?retryWrites=true&w=majority
```
Linux user
```bash
export MONGO_DB_URL=mongodb+srv://Vinit21592:vins21592@cluster0.dl9uoq9.mongodb.net/?retryWrites=true&w=majority
```
then run
```bash
python main.py
```

### Git Commands
#### If you are starting a project and you want to use git in your project
```bash
git init
```
Note: This is going to initalize git in your source code.

OR

#### You can clone exiting github repo
```bash
git clone <github_url>
```
Note: Clone/ Download github repo in your system

#### Add your changes made in file to git stagging area
```bash
git add file_name
```
Note: You can given file_name to add specific file or use "." to add everything to stagging area

#### Create commits
```bash
git commit -m "message"
```
```bash
git push origin main
```
Note: origin--> contains url to your github repo, main--> is your branch name

#### To push your changes forcefully
```bash
git push origin main -f
```

#### To pull changes from github repo
```bash
git pull origin main
```
Note: origin--> contains url to your github repo, main--> is your branch name

### Install Dockers in AWS EC2
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

### High Level Design
URL : https://drive.google.com/file/d/1wh4rMiVD4SKOYl8VPFEqnglU58Sf_23t/view?usp=share_link

### Low Level Design
URL : https://drive.google.com/file/d/1-RshteFJ0hZav62VxL32rXlvKMTaq9Nn/view?usp=share_link

### Architecture Design
URL : https://drive.google.com/file/d/1IsbQUvRRVrCJeCUHRuvzUaT3Xqmy8adS/view?usp=share_link

### Wireframe Document
URL : https://drive.google.com/file/d/1NxoCe7PmTNBXjz1LZHB9r0pRNDG-UCY2/view?usp=share_link

### Detailed Project Report
URL : https://drive.google.com/file/d/1EX3Gst16zFdBDFv3qTnVizoHNiXbxdCL/view?usp=share_link

### Author
Vinit Arun Londhe (LinkedIn: https://www.linkedin.com/in/vinit-londhe21)
