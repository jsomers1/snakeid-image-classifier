#!/bin/sh

# Run this script as "sh automate_prediction.sh 1.jpeg"
FIRST_ARGUMENT="$1"

cd
cd Desktop

# Start container in background from imageID and get containerID
docker run -it -d fab9f44037a5 bash &> snakeID_flask_app/containers.txt
containerNum=$(head -n 1 snakeID_flask_app/containers.txt)

# Copy input image from host to container, ex:
# docker cp Desktop/snakeID_flask_app/static/img/1.jpeg 88bfa7f68368:/test1
A="docker cp snakeID_flask_app/static/img/"
B=" "
C=":/test1"
$A$1$B$containerNum$C

# Run model on image, as in:
#1. docker exec -it --user=root --privileged 21f1f3f252bf7e4976948a834c1dd05d6e233e2ec0199eb5673c83a918a88ace /bin/sh -c "cd /; python tensorflow/tensorflow/examples/image_retraining/label_image.py  --graph=/retrained_graph.pb  --labels=/retrained_labels1.txt  --image=/test1/1.jpeg > prediction.txt"
#2. docker cp 21f1f3f252bf7e4976948a834c1dd05d6e233e2ec0199eb5673c83a918a88ace:/prediction.txt prediction.txt
args=(-it --user=root --privileged "$containerNum" /bin/sh -c "cd /; python tensorflow/tensorflow/examples/image_retraining/label_image.py  --graph=/retrained_graph.pb  --labels=/retrained_labels1.txt  --image=/test1/$1 > prediction.txt")
docker exec "${args[@]}"

# Copy to host
H="docker cp "
I=":/prediction.txt snakeID_flask_app/prediction.txt"
$H$containerNum$I

# Stop and delete container
L="docker stop "
$L$containerNum

Z="docker rm "
$Z$containerNum