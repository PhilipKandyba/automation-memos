#!bin/bash
until $(curl --output /dev/null --silent --head --fail http://localhost:4444 && curl --output /dev/null --silent --head --fail http://localhost:3000 ); do
echo "waiting for selenium hub and react app being started"
sleep 1
done
