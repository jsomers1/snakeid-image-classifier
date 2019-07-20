# SnakeID Image Classifier
<div>
  <img src="snake_images/1.jpeg" width="428" height="298"/>
  <img src="snake_images/2.jpeg" width="428" height="298"/>
</div>
This model uses transfer learning and Google's Inception V3 CNN to classify images of different species of snake. The model classifies images into 2 species classes currently with about 88% accuracy. Future project goals include adding many more species to the image library and continued development of a web app in Flask.

# Table of Contents
* [Tools](#tools)
* [Usage](#usage)
* [Output](#output)

# <a name="tools"></a>Tools
* Docker
* Tensorflow Docker Image
* Flask

# <a name="usage"></a>Usage
* Compile your own image library by web scraping (as in get_images) and through iNaturalist's CSV downloader.
* Rename and restructure image library if necessary
* Download Docker and download Macguyver Tensorflow image
* Run macguyver_model.sh

# <a name="output"></a>Output
| Test Image #1  | Test Image #2 |
| ------------- | ------------- |
| <img src="snake_images/1001.jpg" width="400" height="250"/>  | <img src="snake_images/4609.jpg" width="400" height="250"/>  |
| <img src="snake_images/1001_prediction.png" width="400" height="100"/>  | <img src="snake_images/4609_prediction.png" width="400" height="100"/>  |
