# Machine Learning Path

PacKing apps uses ML model with the case of Object Recognition / Image classification.<br>
This apps uses the model to recognize what the object is and uses the inference to search the design in the packaging design recommendation database.

# Dataset

Because the majority of SMEs in Indonesia is food & beverage business, we make the model to focus on recognizing food & beverage.<br>
We train the model to recognize 20 classes of foods.<br>
The dataset that we use is the combination and modification from 3 sources of dataset.


Here are the datasets those we use:

### 1. Food-11 image dataset
link : https://www.kaggle.com/trolukovich/food11-image-dataset<br>We take 10 classes from this dataset. 

The classes are:
1. Bread
2. Dairy Product -> change folder "Milk"
3. Egg
4. Fried food
5. Meat
6. Noodles-Pasta
7. Rice
8. Seafood
9. Soup
10. Vegetable-Fruit 

### 2. Indonesian Food Dataset
link : https://www.dropbox.com/sh/88stvg9krafl7z8/AAC97IdMbHe7ksp8Cc8I08K2a?dl=0<br>
We take 7 classes from this dataset.

The classes are:

1. Asinan Jakarta
2. Bika Ambon
3. Gudeg
4. Pempek
5. Rendang
6. Sate
7. Surabi


### 3. Food Images (Food-101)
link : https://www.kaggle.com/kmader/food41<br>
We take 3 classes from this dataset.

The Classes are:

1. Donuts
2. Dumplings
3. Macaroni and Cheese


<br>We combine these datasets and did several modification, such as intead of using Diary Product in Food-11 dataset, we use the "Milk" class and get the images from that Diary Product.

# ML Model
We use transfer learing as a method to train the model. We use Inception as the base model and add our own fully connected layer that consists of 5 layers with output layer contains 20 nodes so it can classify the image into one of 20 classes.


How to train the model:
1. Prepare the dataset into training and evaluation dataset. For indonesian food image, we need to divide it into training and evaluation. For the dataset from kaggle, we can easily use it because it's already divided into training and evaluation.
2. initialize the architecture by importing the InceptionV3 for transfer learning.
![initializing](https://i.ibb.co/wwVCGy9/jupy1.png)
3. To add our own classifier (fuly connected layer) to the end of InceptionV3. We need to add flatten layer, so we need to get the output of the last layer from inception
![flatten](https://i.ibb.co/7Spwcc7/jupy2.png)
4. Build our own fully connected layer. In this project we add 5 layers with last layer is output layer which consist of 20 nodes.
![fcl](https://i.ibb.co/LCV3BvZ/jupy3.png)
5. Train the model with ImageDataGenerator. We train the model until 35 epochs and configure the parameters like in this image below
![fcl](https://i.ibb.co/TT1wpL4/jupy4.png)
<br>We get 0,863 validation accuracy and around 0,88 training accuracy<br>
![graph](https://i.ibb.co/kXPHRQM/bangkit.png)
6. To manually test if the model performs well on specific image that we upload, we can use this code
![test](https://i.ibb.co/wRZCcDr/jupy5.png)
