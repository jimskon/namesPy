# namesPy
## A name stats lookup program using a python REST microservice
 - https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
 - https://pypi.org/project/Flask-Cors/
 
## Prequisites
 - Apache2 muct be installed
 - Ports 5000-5005 must be open on the VM firewall

## Setup pip3, Flask and FLASK-CORS
 - ``` sudo apt install python3-pip ```
 - ```sudo apt install python3-flask```
 - ```pip3 install -U flask-cors```

## Install SortedContainers:
 - ``` pip install sortedcontainers ```

## Set Javascript IP address to your VM address
 - Edit ```namelookup.js``` so that ```baseUrl``` is your VM's IP address
 



## Set app (from command line)

 - ```sudo mkdir /var/www/html/namesPy```
 - ```sudo chown ubuntu /var/www/html/namesPy```
 - ```make```
 - ```./start.sh```


