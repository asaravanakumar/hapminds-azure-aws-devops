#!/bin/bash

sudo yum install nodejs-legacy -y
sudo yum install npm -y
#sudo npm install pm2 -g

#create our working directory if it doesnt exist
DIR="/home/ec2-user/nodeapp"
if [ -d "$DIR" ]; then
  echo "${DIR} exists"
else
  echo "Creating ${DIR} directory"
  mkdir ${DIR}
fi