# Cloud

## Flow Diagram

![diagram](https://i.ibb.co/B3xrsb4/Pac-King-FIX.png)

<br/>

## Login Mechanism

For Android login mechanism, we use Identity Platform from Google Cloud Platform connected via Firebase Authentication. <br/><br/>
**1. To get started you can go to the GCP console, then enable Identity Platform.**

![IdentityPlatform](https://i.ibb.co/ZmYkPTJ/Identity-Platform.png)
<br/><br/>
**2. Then you have to add a provider by clicking "ADD A PROVIDER".**

![AddProvider](https://i.ibb.co/61q7pcw/add-provider.png)
<br/><br/>

**3. Then in the Sign-in method, enable Email / Password login, then save your configuration.**

![SignInMethod](https://i.ibb.co/r4dVYXJ/Sign-in-method.png)

**4. After that, click "APPLICATION SETUP DETAILS". You will enter the application configuration page. On that page select the ANDROID tab then select "Get Started In Firebase".**


![Setup](https://i.ibb.co/Y2xWWNP/Setup-detail.png)

![Configure](https://i.ibb.co/Nx3wrzP/Configure.png)

**5. In the Firebase Console you must add your Android app to your Firebase project. You can follow the steps provided by Firebase as shown below.**

![RegisterApp](https://i.ibb.co/2nPKGnG/Register-APP.png)

![LoginJSON](https://i.ibb.co/mJ9k1rG/download-JSON-login.png)

![SDK](https://i.ibb.co/fnR9GwL/add-SDK.png)

**6. Then on the "Build" tab in your project select "Authentication".**

![FirebaseAuth](https://i.ibb.co/mDF3kzQ/Firebase-Auth.png)

**7. Then in the Sign-in-method section, activate the Email / Password provider, then save your configuration.**

![EnableLogin](https://i.ibb.co/Byp6QVv/Enable-Email.png)

**After that you have to configure Realtime Database to store user data.**


## User Data Storage

For user data storage, you can enable Firebase Realtime Database. <br/><br/>

**1. To get started, on the "Build" tab select Realtime Database. Then create a new database.**

![database](https://i.ibb.co/Ksypx1w/Realtime-Database.png)

**2. Then configure your database by selecting the location and the rules. Then click Enable.**

![setupdatabase](https://i.ibb.co/kg5zhrM/Setup-Database.png)

![setupdatabase2](https://i.ibb.co/FxJc1NH/Setup-Database-2.png)

Your database can be used to store user data such as email and passwords, as well as other user data in the application.

## Storage for Application Images and Machine Learning Models

For storage of machine learning models and application images, such as photos from users, as well as images of design recommendations we use Cloud Storage.

**1. To get started, you can head to the Google Cloud Console and create a new bucket in Cloud Storage.**

![bucket](https://i.ibb.co/z4879ct/bucket.png)

**2. Then set your bucket configuration according to your needs, then click create and your bucket is ready to use .**

Note: For machine learning model storage buckets that you will use on the AI platform or Vertex AI, you must pay attention to the region of the bucket. To be able to upload models to the platform, the region of the bucket must match the region of the platform you set.
You also need JSON key for Android, so the Android client can access the bucket. You can create a Service Account and import the JSON key to the Android.

![createbucket](https://i.ibb.co/jLzbj4k/create-bucket.png)

## Deploy the Machine Learning Models
 
To deploy machine learning, we use Vertex AI. The reason we use Vertex AI is because it can accept custom trained models and can easily manage its endpoints.

**1. To get started, you can go to the Console and enable the Vertex AI Platform.**

![enablev](https://i.ibb.co/sj7jNVn/enable.png)

**2. Then in the sidebar, select models and select Import model.**

![models](https://i.ibb.co/YjKpHsc/models.png)

![import](https://i.ibb.co/b2PLmv9/import.png)

**3. Then set the model settings according to your needs, then click "Import".**
Note: If you want to import models from Cloud Storage, make sure you select the same region as your Storage.

![setmodel](https://i.ibb.co/M92HQsq/set1.png)

![setmodel2](https://i.ibb.co/mHVG7mL/set2.png)

**4. After the model imported, you will need to create enpoint to deploy your model. Click deploy to endpoint to start creating new endpoint.**

![endpoint](https://i.ibb.co/QkL21tH/endpoint.png)

**5. Then set the endpoint settings according to your needs, then click "DEPLOY", and your model is ready.**

![deploy1](https://i.ibb.co/XpYJVNS/deploy1.png)

![deploy2](https://i.ibb.co/R2WrrGF/deploy2.png)

## Create Cloud Function

To run the AI model and give response to Android client, you will need to make a Cloud Function.

**1. To get started, you can go to the console and enable the Cloud Function by Create a new function.**

![create](https://i.ibb.co/zr6W87g/Create.png)

**2. Then set the Cloud Function configuration according to your needs. In this project we use HTTP trigger and allow unauthenticated invocations.

![conf](https://i.ibb.co/JCb2q6Y/conf.png)

**3. Then for the Runtime, we add new variable that we will use in the function, named ENDPOINT_ID and the value is the endpoint id that you already created in the Vertex AI.**

![runtime](https://i.ibb.co/nP6hTy7/runtime.png)

**4. Then we will make our function. In this project we use Python 3.7 runtime. You can find the code and requirements for the function [Here](https://github.com/alfiyansyah776/PacKing/tree/main/CloudLP/Function). Then click "DEPLOY" and your Cloud Function is ready to use.** 

![code](https://i.ibb.co/gJCxDyG/code.png)
