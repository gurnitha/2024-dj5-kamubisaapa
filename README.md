# 2024-dj5-kamubisaapa
Membuat A REAL WORLD PROJECT: Aplikasi untuk memajang hasil karya orang-orang kreatif


## 1. CLONE REMOTE REPOSITORY


#### 1. Meng-clone remote repositori dan commit lokal repositori

        C:\Users\ING\Desktop\2024-DEVSPACE
        λ git clone git@github.com:gurnitha/2024-dj5-kamubisaapa.git
        Cloning into '2024-dj5-kamubisaapa'...
        Enter passphrase for key '/c/Users/ING/.ssh/id_rsa':
        remote: Enumerating objects: 4, done.
        remote: Counting objects: 100% (4/4), done.
        remote: Compressing objects: 100% (4/4), done.
        remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
        Receiving objects: 100% (4/4), done.

        C:\Users\ING\Desktop\2024-DEVSPACE
        λ ls
        2024-dj5-kamubisaapa/

        modified:   README.md


## 2. MEMBUAT LINGKUNGAN VIRTUAL


#### 1. Membuat lingkungan virtual

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-kamubisaapa(main -> origin)
        λ REM: Membuat lingkungan virtual atau local environment

        λ python --version
        Python 3.12.1

        λ pip --version
        pip 24.0 from E:\_WORKSPACE\laragon\bin\python\python-3.12\Lib\site-packages\pip (python 3.12)

        λ python -m venv venv312502 --promp bisaapa

        modified:   .gitignore
        modified:   README.md


#### 2. Mengaktifkan venv312502

        λ REM: Mengaktifkan venv312502

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-kamubisaapa(main -> origin)
        λ ls
        README.md  venv312502/

        λ venv312502\Scripts\activate.bat

        (bisaapa) λ


## 3. MENGINSTAL DJANGO


#### 1. Menginstal django versi 5.0.2

        (bisaapa) λ REM: Menginstal django versi 5.0.2

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-kamubisaapa(main -> origin)
        (bisaapa) λ pip install django==5.0.2
        ...
        Successfully installed asgiref-3.7.2 django-5.0.2 sqlparse-0.4.4 tzdata-2024.1

        [notice] A new release of pip is available: 23.2.1 -> 24.0
        [notice] To update, run: python.exe -m pip install --upgrade pip


#### 2. Memeriksa hasil instalasi

        (bisaapa) λ REM: Memeriksa hasil instalasi

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-kamubisaapa(main -> origin)
        (bisaapa) λ pip freeze
        asgiref==3.7.2
        Django==5.0.2
        sqlparse==0.4.4
        tzdata==2024.1


## 4. MEMEBUAT PROYEK DJANGO


#### 1. Membuat proyek django dengan nama 'config'

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 2. Menjalankan kali pertama server django 

        (bisaapa) λ REM: Menjalankan kali pertama server django

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-kamubisaapa(main -> origin)
        (bisaapa) λ ls
        config/  manage.py*  README.md  venv312502/

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-kamubisaapa(main -> origin)
        (bisaapa) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        February 27, 2024 - 10:12:35
        Django version 5.0.2, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.


#### 3. Membuka laman default bawaan django di browser

        http://127.0.0.1:8000/


## 5. MEMEBUAT APLIKASI DJANGO


#### 1. Membuat aplikasi django dengan nama 'projects' di dalam folder app

        modified:   README.md
        new file:   app/projects/__init__.py
        new file:   app/projects/admin.py
        new file:   app/projects/apps.py
        new file:   app/projects/migrations/__init__.py
        new file:   app/projects/models.py
        new file:   app/projects/tests.py
        new file:   app/projects/views.py


#### 2. Instal aplikasi projects pada config/settings.py

        modified:   README.md
        modified:   app/projects/apps.py
        modified:   config/settings.py


## 6. HALLO WORLD, HALLO TEMAN


#### 1. Membuat hallo_world views

        modified:   README.md
        modified:   app/projects/views.py


#### 2. Membuat urls untuk hello_world views

        modified:   README.md
        new file:   app/projects/urls.py


#### 3. Memasang projects/urls.py pada config/urls.py

        modified:   README.md
        modified:   config/urls.p


#### 4. Menjalankan server dan melihat hasilnya

        (bisaapa) λ REM: Memeriksa hasilnya dan menjalankan server

        (bisaapa) λ python manage.py check
        System check identified no issues (0 silenced).

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5-kamubisaapa(main -> origin)
        (bisaapa) λ python manage.py runserver
        ...
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.


## 7. DATABASE


#### 1. Start dan masuk ke server

        λ REM: Masuk ke server sebagai root user tanpa password

        E:\_WORKSPACE\laragon\bin\cmder
        λ mysql -u root
        Welcome to the MySQL monitor.  Commands end with ; or \g.
        Your MySQL connection id is 8
        Server version: 8.0.30 MySQL Community Server - GPL

        Copyright (c) 2000, 2022, Oracle and/or its affiliates.

        Oracle is a registered trademark of Oracle Corporation and/or its
        affiliates. Other names may be trademarks of their respective
        owners.

        Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

        mysql>


#### 2. Create db

        mysql> SHOW DATABASES;                            
        +-------------------------------------------+     
        | Database                                  |     
        +-------------------------------------------+     
        | 2024_db_1                                 |     
        | 2024_db_2                                 |     
        ...  
        | sys                                       |     
        | test_db                                   |     
        | w3schools                                 |     
        +-------------------------------------------+     
        38 rows in set (0.06 sec)                         
                                                          
        mysql> CREATE DATABASE 2024_dj5_kamubisaapa;      
        Query OK, 1 row affected (0.09 sec)               
                                                          
        mysql> SHOW DATABASES;                            
        +-------------------------------------------+     
        | Database                                  |     
        +-------------------------------------------+     
        | 2024_db_1                                 |     
        | 2024_db_2                                 |       
        | 2024_dj5_kamubisaapa                      |     
        ...   
        | sys                                       |     
        | test_db                                   |     
        | w3schools                                 |     
        +-------------------------------------------+     
        39 rows in set (0.00 sec)                         
                                                          
        mysql>


#### 3. Konek db dengan proyek

        modified:   README.md
        modified:   config/settings.py

        ...
        Did you install mysqlclient? 


#### 4. Meng-upgrade pip   

        (bisaapa) λ python.exe -m pip install --upgrade pip
        ...
        Successfully installed pip-24.0  


#### 5. Memeriksa koneksi db dengan proyek dengan menjalankan server

        (bisaapa) λ REM: Memeriksa koneksi db dengan proyek dengan menjalankan server

        (bisaapa) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        February 27, 2024 - 11:56:15
        Django version 5.0.2, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.


## 8. MELINDUNGI FILE SENSITIF


#### 1. Menggunakan django-environ untuk melindungi sensitif file

        Steps 1: instal django-environ
        (bisaapa) λ python -m pip install django-environ

        Steps 2: create .env .env-example
        (bisaapa) λ touch .env .env-example

        Steps 3: set up .env file
        DEBUG=True
        SECRET_KEY=django-insecure-httc#cur2tsn2qq*zhu$%d+*gtm21u4l=$p(_$!5+8ukcgo&k2
        DATABASE_NAME=2024_dj5_kamubisaapa
        DATABASE_USER=root
        DATABASE_PASSWORD=
        DATABASE_HOST=localhost
        DATABASE_PORT=3306

        # Step 4: setup config/settings.py
        # 1. import environ dan os
        import environ
        import os

        # 1. Create environ
        env = environ.Env(
            # set casting, default value
            DEBUG=(bool, False)
        )

        # 2. Set the project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # 3. Take environment variables from .env file
        environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

        # 4. False if not in os.environ because of casting above
        DEBUG = env('DEBUG')

        # 5. Raises Django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
        SECRET_KEY = env('SECRET_KEY')

        # 6. Set db
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': os.environ.get('DATABASE_NAME'),
                'USER': os.environ.get('DATABASE_USER'),
                'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
                'HOST': os.environ.get('DATABASE_HOST'),
                'PORT': os.environ.get('DATABASE_PORT'),
            }
        }

        Step 5: run python manage.py check
        (bisaapa) λ python manage.py check

        The result:
        System check identified no issues (0 silenced).

        new file:   .env-example
        modified:   README.md
        modified:   config/settings.py


## 9. DJANGO ADMIN


#### 1. Mengaktifkan django admin dengan menjalan migrasi

        (bisaapa) λ python manage.py makemigrations
        (bisaapa) λ python manage.py migrate


#### 2. Membuat superuser

        (bisaapa) λ REM: Membuat superuser
        (bisaapa) λ python manage.py createsuperuser
        Username (leave blank to use 'ing'): superuser
        Email address: superuser@mail.com
        Password:
        Password (again):
        The password is too similar to the email address.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.

        mysql> SELECT username, is_superuser FROM auth_user;
        +-----------+--------------+
        | username  | is_superuser |
        +-----------+--------------+
        | superuser |            1 |
        +-----------+--------------+
        1 row in set (0.00 sec)


#### 3. Login as superuser

        http://127.0.0.1:8000/admin/
        use your createsuperuser username and  password to login


## 10. DJANGO MODEL


#### 1. Membuat model: Project

        modified:   README.md
        modified:   app/projects/models.py


#### 2. Menjalankan migrasi membuat tabel

        (bisaapa) λ REM: Membuat tabel projects

        (bisaapa) λ python manage.py makemigrations
        Migrations for 'projects':
          app\projects\migrations\0001_initial.py
            - Create model Project

        (bisaapa) λ python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, projects, sessions
        Running migrations:
          Applying projects.0001_initial... OK

        (bisaapa) λ python manage.py sqlmigrate projects 0001
        --
        -- Create model Project
        --
        CREATE TABLE `projects_project` (
                `title` varchar(200) NOT NULL,
                 `description` longtext NULL,
                 `demo_link` varchar(2000) NULL, 
                 `source_link` varchar(2000) NULL, 
                 `created` datetime(6) NOT NULL, 
                 `id` char(32) NOT NULL PRIMARY KEY
        );

        mysql> DESC projects_project;
        +-------------+---------------+------+-----+---------+-------+
        | Field       | Type          | Null | Key | Default | Extra |
        +-------------+---------------+------+-----+---------+-------+
        | title       | varchar(200)  | NO   |     | NULL    |       |
        | description | longtext      | YES  |     | NULL    |       |
        | demo_link   | varchar(2000) | YES  |     | NULL    |       |
        | source_link | varchar(2000) | YES  |     | NULL    |       |
        | created     | datetime(6)   | NO   |     | NULL    |       |
        | id          | char(32)      | NO   | PRI | NULL    |       |
        +-------------+---------------+------+-----+---------+-------+
        6 rows in set (0.00 sec)

        modified:   README.md
        new file:   app/projects/migrations/0001_initial.py


#### 3. Register Project model pada admin.py

        modified:   app/projects/admin.py


#### 4. Add data proyek dari admin dashboard

        modified:   README.md