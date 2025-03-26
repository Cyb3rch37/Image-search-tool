This tool helps you find images of yourself that have been posted on the web without your knowledge, using facial recognition software and Beautiful Soup..
```
Here is the installation guide:
Install Docker
  sudo apt update

Install Required Packages  
  sudo apt-get install -y \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg \
  lsb-release

Add Docker’s official GPG key:
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

Set up the stable repository:
  echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Update the package Inndex Again
  sudo apt update

Install Docker Engine
  sudo apt-get install docker-ce docker-ce-cli containerd.io

Verify that Docker Engine is installed correctly by running the hello-world image.
  sudo docker run hello-world

Install Docker Compose    

Download the Docker Compose binary
  sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep -Po '"tag_name": "\K.*?(?=")')/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

Apply executable permissions to the binary
  sudo chmod +x /usr/local/bin/docker-compose

Verify the installation by running the following command which will display the Docker Compose version:
  docker-compose --version

Clone the repository
  git clone https://github.com/Cyb3rch37/Image-search-tool.git

Change the directory
  cd Image-search-tool

Create a python virtual environment
  python3 -m venv (your virtual environment name)

Activate the virtual environment
  source (your virtual environment name)/bin/activate

Install django
  pip install django

Create a .env file to hide sensitive infomation in your root directory of the project i.e where your manage.py file is located.
  touch .env

Add your API keys to the .env file

Install python-dotenv
  pip install python-dotenv

Build the docker image
  docker-compose up --build

Steps to Build Your Image Search Tool API

Set Up Django and Django REST Framework (DRF)
  Install Django and Django REST Framework
  pip install django djangorestframework pillow numpy opencv-python

Create an API Endpoint for Image Search

Implement Image Search Logic (Using Feature Matching or Hashing)

Integrate External APIs (Optional)

Deploy the API (Optional)


