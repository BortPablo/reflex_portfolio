sudo yum install nginx
sudo systemctl start nginx
sudo systemctl enable nginx
sudo cp nginx.conf /etc/nginx/conf.d/
sudo systemctl reload nginx

