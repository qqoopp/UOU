# UOU

라즈베리파이 초기 설치 절차 입니다.
1. update, upgrade

pi@raspberrypi:~ $ sudo apt-get update
pi@raspberrypi:~ $ sudo apt-get dist-upgrade

2. Remove unused packages

sudo apt-get remove python2.7
sudo apt-get purge realvnc-vnc-*
sudo apt-get remove --purge libreoffice-*
sudo apt-get remove --purge wolfram-engine
sudo apt-get autoremove
sudo apt-get clean

3. install packages

sudo apt-get install git	
sudo apt-get install xrdp	
sudo apt-get install ntp
sudo apt install python3.6

4. install python packages

pip3 install --upgrade pip
pip3 install Django
pip3 install requests
pip3 install network	

