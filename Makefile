# MakeFile to deploy the Sample US CENSUS Name Data 
# server using Python Microservice
# For MATH318 Software Development

all: PutHTML

PutHTML:
	cp namelookup.html /var/www/html/namesPy/
	cp namelookup.css /var/www/html/namesPy/
	cp namelookup.js /var/www/html/namesPy/

	echo "Current contents of your HTML directory: "
	ls -l /var/www/html/namesPy/
