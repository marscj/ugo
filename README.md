# /ect/nginx/conf.d/nginx.conf
server {
        listen 80;
        server_name ugodubai.tk www.ugodubai.tk;
        location / {
                proxy_pass http://localhost:8080;
        }
}

# ugo
$ docker-compose build
$ docker-compose up -d

# Linux 安装
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

$ sudo chmod +x /usr/local/bin/docker-compose

$ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose  $ docker-compose --version

Or
$ sudo python3 -m pip install docker-compose