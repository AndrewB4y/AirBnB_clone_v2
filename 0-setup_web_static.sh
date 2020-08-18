#!/usr/bin/env bash
# setting up a web server for a web_Static deployment

sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/release
sudo mkdir -p /data/web_static/share
sudo mkdir -p /data/web_static/releases/test
echo "<html>
    <head>
    </head>
    <body>
        Testing config...
    </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '0,/location \/ {/ s/location \/ {/location \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;/' /etc/nginx/sites-available/default
service nginx restart
