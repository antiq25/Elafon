 m███  ███      ███████████ ███████████   █████ ██████████   ██████████ ██████   █████ ███████████   
 ████████████   ░█░░░███░░░█░░███░░░░░███ ░░███ ░░███░░░░███ ░░███░░░░░█░░██████ ░░███ ░█░░░███░░░█   
░░░███░░███░    ░   ░███  ░  ░███    ░███  ░███  ░███   ░░███ ░███  █ ░  ░███░███ ░███ ░   ░███  ░    
 ████████████       ░███     ░██████████   ░███  ░███    ░███ ░██████    ░███░░███░███     ░███       
░░░███░░███░        ░███     ░███░░░░░███  ░███  ░███    ░███ ░███░░█    ░███ ░░██████     ░███       
  ░░░  ░░░          ░███     ░███    ░███  ░███  ░███    ███  ░███ ░   █ ░███  ░░█████     ░███       
                    █████    █████   █████ █████ ██████████   ██████████ █████  ░░█████    █████      
                   ░░░░░    ░░░░░   ░░░░░ ░░░░░ ░░░░░░░░░░   ░░░░░░░░░░ ░░░░░    ░░░░░    ░░░░░       
                                                                                                     
    TRIDENT INVENTORY MANAGEMENT SYSTEM VERSION 1.0 - COPYRIGHT ELAFON MECHANICAL LTD 2023 -  ALL RIGHTS RESERVED.

    THE FOLLOWING BELOW IS A DETAILED MANUAL AND GUIDE ON HOW THE PROGRAM FUNDAMENTALLY WORKS AS OF AUGUST 16/2023. 

    DOCUMENT WILL CONTINUE TO BE UPDATED AS PER CHANGES ARE MADE.

    DOC @ https://docs.google.com/document/d/10Euv9NMti_Cj0xeq0pIowHzddLBA2gfhh9RblvWhBis/edit

# LAYOUT AND FILE STRUCTURE   

All files must be served with these paths in mind.

 STATIC - - > hosts your themes, images, javascript

 TEMPLATES - - > hosts your .html files (your webpage)

 APP.PY - - > your server side code. 

├── Elafon
├──  templates
│       └─   .html files (web pages) 
             └─  base.html (core template of application) 
│             
├──  static
│         ├──  css (theme + grid ) 
│         ├──  js (javascript)      
│         ├── images             
├──  app.py
├──  .env (Configuration for app.py)
├──  requirements.txt (Package list for pip)
│
├──  instance 
├     └─   database < -- database file this will contain all of the item id's etc / logins / anything ├related to to stored information 




FRESH INSTALL + TESTING ON LOCAL MACHINE 
- make sure pip (python package manager, and virtualenv (virtual environment is installed on your machine) 
- open terminal that has git installed in it.
- git clone http://github.com/antiq25/Elafon ( this is the source code ) 

- navigate to the director * type cd ~/Elafon 
- create virtual environment * type  virtualenv env
- install dependencies  * type  pip install -r requirements.txt 

Run the application  * type python3 app.py (you can open the app in the browser @ 127.0.0.1:5000 ) 




