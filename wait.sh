#!bin/bash
until $(curl --output /dev/null --silent --head --fail http://selenium-hub:4444/wd/hub && curl --output /dev/null --silent --head --fail http://memos:5230 ); do
echo "Waiting for selenium hub and react memo being started"
sleep 1
done
