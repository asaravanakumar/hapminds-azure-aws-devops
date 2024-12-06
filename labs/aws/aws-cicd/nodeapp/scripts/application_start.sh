#!/bin/bash

sudo chmod -R 777 /home/ec2-user/nodeapp
cd /home/ec2-user/nodeapp
npm install
npm start > app.out.log 2> app.err.log < /dev/null &