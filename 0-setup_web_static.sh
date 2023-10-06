#!/usr/bin/env bash
#0. Prepare your web servers

sudo apt-get update
sudo apt-get install nginx -y

sudo ufw allow 'Nginx HTTP'


sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

target='/data/web_static/releases/test/'
link='/data/web_static/current'
if [ -L "link" ];
	then
	sudo rm "$link"
fi
sudo ln -s "$target" "$link"

sudo chown -R ubuntu:ubuntu /data/


sudo sed -i 's|location /hbnb_static/ {|location /hbnb_static/ {\n    alias /data/web_static/current/;|' /etc/nginx/sites-available/default


sudo fuser -k 80/tcp
sudo nginx -t
sudo systemctl restart nginx
