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