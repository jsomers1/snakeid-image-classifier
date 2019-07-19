# Pull from repo and set up tensorflow container
docker run -it -d macgyvertechnology/tensorflow
docker images

# View containers
docker ps -a

# To kill container
# docker stop _containerIDnum_

# Copy training and testing images to container
#docker rm -rf /training_images/*
docker cp Desktop/training_images1/ _containerIDnum_:/
docker cp Desktop/retrained_labels1.txt _containerIDnum_:/
docker cp Desktop/test1/ _containerIDnum_:/

# Check directories in container are correct
docker exec -it _containerIDnum_ bash
cd /



# Train model
python tensorflow/tensorflow/examples/image_retraining/retrain.py  --bottleneck_dir=/bottlenecks  --model_dir=/inception  --output_labels=/retrained_labels1.txt  --output_graph=/retrained_graph.pb  --image_dir=/training_images1



# Testing
python tensorflow/tensorflow/examples/image_retraining/label_image.py  --graph=/retrained_graph.pb  --labels=/retrained_labels.txt  --image=/test1/1050.jpg
python tensorflow/tensorflow/examples/image_retraining/label_image.py  --graph=/retrained_graph.pb  --labels=/retrained_labels.txt  --image=/test1/827.jpg
python tensorflow/tensorflow/examples/label_image/label_image.py \

# set up web app in flask
# take in user submitted image
# send via API to container
# container downloads image
# runs trained model in docker image on input image
# output percentages



# see if model can be downloaded
# write script that takes new image, runs on model
# output percentages
# integrate all of this into web app
