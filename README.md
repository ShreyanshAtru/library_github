# library_github
# A basic library management system , where User login a s a super user and can add, delete , update a book.

there are two tables 
    - User 
    - Book 
To access the project , clone the repostiry in your local system by 
    - git clone https://github.com/ShreyanshAtru/library_github.git

Firstly create a virtual environment and activate 
    - pip install virtualenv  # windows 
    - virtualenv <env_name>
    - .\<env_ame>\Scripts\activate
    
Run the requriements file for dependcies 
    - pip install -r requirements.txt 
    
After this go to the project directory where you can see manage.py file and run these commads 
    - python manage.py makemigrations 
    - python manage.py migrate 
    - python manage.py runserver 
   
