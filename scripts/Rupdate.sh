#!/bin/bash

#Get latest R version

clear

echo "updating R-base"
sudo apt-key adv –keyserver keyserver.ubuntu.com –recv-keys E084DAB9
sudo add-apt-repository ‘deb http://star-www.st-andrews.ac.uk/cran/bin/linux/ubuntu trusty/’
sudo apt-get update
sudo apt-get install r-base

wait 10
# Download and install RStudio

echo"installing RStudio"
sudo apt-get install libjpeg62
wget http://download1.rstudio.org/rstudio-0.98.1062-amd64.deb
sudo dpkg -i *.deb
rm *.deb

echo "all done"
wait 10
clear
