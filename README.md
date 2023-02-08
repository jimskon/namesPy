# namesPy
## A name stats lookup program using a python REST microservice

## Prequisites
 - Apache2 muct be installed
 - Ports 5000-5005 must be open on the VM firewall

## Setup pip3, Flask and FLASK-CORS
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

## Set Javascript IP address to your VM address
 - Edit ```namelookup.js``` so that ```baseUrl``` is your VM's IP address
 
https://pypi.org/project/Flask-Cors/

## Install pip and SortedContainers:
 - ``` sudo apt install python3-pip ```
 - ``` pip install sortedcontainers ```


## Set app (from command line)
 - ```sudo apt install python3-flask```
 - ```pip3 install -U flask-cors```
 - ```sudo mkdir /var/www/html/namesPy```
 - ```sudo chown ubuntu /var/www/html/namesPy```
 - ```make```
 - ```./start.sh```


