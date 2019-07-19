# SnakeID Image Classifier
<div>
  <img src="snake_images/1.jpeg" width="428" height="298"/>
  <img src="snake_images/2.jpeg" width="428" height="298"/>
</div>
This model uses transfer learning and Google's Inception V3 CNN to classify images of different species of snake. The model classifies images into 2 species classes currently with about 88% accuracy. Future project goals include adding many more species to the image library and continued development of a web app in Flask.

# Table of Contents
* [Requirements](#requirements)
* [Usage](#usage)
* [Output](#output)

# <a name="requirements"></a>Tools
* Docker
* Tensorflow Docker Image
* Flask

# <a name="usage"></a>Usage
* Compile your own image library by web scraping (as in get_images) and through iNaturalist's CSV downloader.
* Rename and restructure image library if necessary
* Download Docker and download Macguyver Tensorflow image
* Run macguyver_model.sh

# <a name="output"></a>Output
* Test image #1            * Test image #2
<div>
  <img src="snake_images/827.jpg" width="100" height="100"/>
  <img src="snake_images/1050.jpg" width="100" height="100"/>
</div>
