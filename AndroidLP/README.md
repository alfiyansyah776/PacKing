# PacKing Android LP

This application needs two credentials to work properly, the first one is API <br>key to authenticate to Firebase and the second one is to authenticate to Google Cloud.

How to obtain those two files already explained in Cloud Readme section.

## Firebase Configuration

* After you get the JSON File from Google Firebase, you can put the file to app folder like this example

![API Key Location](https://i.imgur.com/0kZYAVQ.png)

* As for JSON file, it supposed to looked like this 

![API Key Format](https://i.imgur.com/rYZMsfb.png)

* We suggest you to make database on Firebase with structure like this one

![API Key Format](https://i.imgur.com/AhY7fMn.png)

## Google Cloud Configuration

* You can put the JSON File from Google Cloud to *assets* folder like this one.

![API Key Format](https://i.imgur.com/S6l9N3h.png)

* As for format, it suppose to looked like this

![JSON GCP](https://i.imgur.com/LSdqW3g.png)

* You can change this line of code (on MainActivity.kt) and make it same as your JSON file's name

```val storage: Storage? = UploadImageHelper.setCredentials(assets.open("GoogleMapDemo.json"))```

## Upload and Retrieve Image Recommendation Mechanism

You need at least one bucket to upload your image and same recommendation folder there.

![GCP Bucket](https://i.imgur.com/sGJztA8.png)

### Upload Image to bucket


### Retrieve JSON file from cloud





