# SnakeID Image Classifier
<div>
  <img src="snake_images/1.jpeg" width="428" height="298"/>
  <img src="snake_images/2.jpeg" width="428" height="298"/>
</div>

This model uses transfer learning and Google's Inception V3 convolutional neural network to classify images of different species of the suborder *Serpentes*, specifically those of the genus *Agkistrodon*. The model currently classifies 2 species classes with about 89% overall accuracy. A web application written with Flask and HTML serves as a GUI for the model, whose code is found on a Docker image.

# Table of Contents
* [Tools](#tools)
* [Methodology](#method)
* [Example Output](#eoutput)
* [Front-End Application](#views)

# <a name="tools"></a>Tools
* Python
* Docker
* Tensorflow Docker Image (from Macgyver)
* Flask
* HTML

# <a name="method"></a>Methodology
* Compiled image library by web scraping (get_images.py) and through iNaturalist's CSV downloader
* Renamed and restructured image library for 2 image classes
* Downloaded Docker and Macgyver Tensorflow Docker image
* Ran various commands from macgyver_model.sh to import, train, and test model on image library
<table align="center">
<tr>
<td align="center">Overall Model Accuracy</td>
<td align="center"><img src="snake_images/overall_accuracy.png" width="600" height="25"/><br/></td>
</tr>
</table>

* Implemented web application with Flask and HTML to receive the user's image input and interface with model locally


# <a name="eoutput"></a>Example Output
| Test Image #1  | Test Image #2 |
| ------------- | ------------- |
| <img src="snake_images/1001.jpg" width="400" height="250"/>  | <img src="snake_images/4609.jpg" width="400" height="250"/>  |
| <img src="snake_images/1001_prediction.png" width="400" height="65"/>  | <img src="snake_images/4609_prediction.png" width="400" height="65"/>  |




# <a name="views"></a>Front-End Application
<kbd>
  <img src="snake_images/web_view1.png" width="900" height="450"/>
</kbd>
<kbd>
  <img src="snake_images/web_view2.png" width="900" height="550"/>
</kbd>
