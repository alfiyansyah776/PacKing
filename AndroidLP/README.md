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

To upload an image to bucket, we need google credential name GoogleMapDemo.json and a function name UploadImageHelper. That function has task to
open the GCP bucket and upload that file image to the bucket. The function look like this :

![CODE](https://i.imgur.com/EaqGFl6.jpg)


### Post JSON file to Deployed AI Model
After upload image to the bucket, we need to upload a JSON file which contain an image URL from GCP bucket to deployed AI model, this process handled by 
a POST function using volley in OnActiivityResult function, it looks like this :

![CODE](https://i.imgur.com/IHuwFAu.jpg)

with this code we get variable name "idRekomendasi", that variable is important to get recommendation design.


### Get Recommended design from AI Model

With variable idRekomendasi we can get the recommendation design by send that variable to RekomendasiActivity via intent. After that, idRekomendasi become the
parameter to the function that retrieve the design recommendation. That function is in RekomendasiViewModel, it look like this :

* Function in RekomendasiViewModel
![CODE](https://imgur.com/0vKtsq2.jpg)



* Function to get design recommendation

![CODE](https://imgur.com/NzGt2F5.jpg)

