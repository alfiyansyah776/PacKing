# Cloud

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

![createbucket](https://i.ibb.co/jLzbj4k/create-bucket.png)




