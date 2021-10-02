# fasttext-language-detection
Fasttext language detection wrapped in Fastapi + Docker🐋

### 1. Go to project dir

```shell
git clone https://github.com/Jason-Oleana/fasttext-language-detection.git
cd fasttext-language-detection
```

### 2. Build

```shell
sudo docker-compose build
```
wait...

### 3. Run project

##### 3.1 Run with logs in console

```shell
sudo docker-compose up
```

##### 3.2 Run as process

```shell
sudo docker-compose up -d
```

### 4. Other Docker commands

##### 4.1 Stop containers
```shell
sudo docker-compose down
```

##### 4.2 Restart containers
```shell
sudo docker-compose restart
```


##### 4.3 Remove image
```shell
sudo docker rmi [image-name]
```
or
```shell
sudo docker rmi -f [image-name]
```

##### 4.4 Show Docker process
```shell
sudo docker ps
sudo docker-compose ps
```

##### 4.5 Show Docker images
```shell
sudo docker images
sudo docker-compose images
```