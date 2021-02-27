# con-heal
A medical app (time-track) to connect pymysql with MySQL (localhost connection) and with a ssh server (LAN connection).
I chose an intranet infrastructure for security reasons. Of course, it's possible to extend internet connection with forwarding on server.

# How to use MySQL

> systemctl status mysql \
> systemctl start mysql \
> systemctl stop mysql

# MySQL workbench (config)

1) Create a database :
MYSQL Connections --> click '+'
2) Enter connection name and password
3) Click on 'Test connection'
Password required
4) Create a table
Latin-1 or Utf-8
5) Create columns
6) Save model
7) Return to 'home' and click on your new connection

# How to install pymysql

Install python3-pymysql :
> sudo apt install python3-pymysql

Install pymysql in virtualenv :
> pip3 install pymysql (or PyMySQL)

# Prepares to launch app :
To start ssh connection :
> ssh -i ~/publickeyshared server@192.168.XX.XX \
To start mysql :
> sudo systemctl start mysql \
or \
> sudo /etc/init.d/mysql start

Already done... (look at requirements.txt)

# Launch app with :
> python3 heal_track.py

# Still under development !
(It should be finished by june 2021)

ko@l@tr33
