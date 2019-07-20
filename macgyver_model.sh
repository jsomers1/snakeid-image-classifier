# First time: pull from repo and set up tensorflow container
docker run -it -d macgyvertechnology/tensorflow
docker images

# To continue working with previously used images
docker run -it fab9f44037a5 bash # or also 173a0562871e

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
ls

# Train model
python tensorflow/tensorflow/examples/image_retraining/retrain.py  --bottleneck_dir=/bottlenecks  --model_dir=/inception  --output_labels=/retrained_labels1.txt  --output_graph=/retrained_graph.pb  --image_dir=/training_images1

# Test on sample images
python tensorflow/tensorflow/examples/image_retraining/label_image.py  --graph=/retrained_graph.pb  --labels=/retrained_labels.txt  --image=/test1/1050.jpg
python tensorflow/tensorflow/examples/image_retraining/label_image.py  --graph=/retrained_graph.pb  --labels=/retrained_labels.txt  --image=/test1/827.jpg
python tensorflow/tensorflow/examples/label_image/label_image.py \

# Use for copying to / from Docker and host
# docker cp _containerIDnum_:/test1/1001.jpg /Users/js/Desktop
