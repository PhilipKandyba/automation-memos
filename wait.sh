#!bin/bash
until $(curl --output /dev/null --silent --head --fail http://localhost:4444 && curl --output /dev/null --silent --head --fail http://localhost:5230 ); do
echo "Waiting for selenium hub and memo being started"
sleep 1
done
