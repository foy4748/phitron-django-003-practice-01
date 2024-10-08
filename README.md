# Instructions    

- DEMO Video - [Google Drive](https://drive.google.com/file/d/14p7U6E0JJkwsQADkpDUECc65vdmUwKWw/view?usp=drive_link)

- Requirement Doc **Module 14.5** : [Google Doc](https://docs.google.com/document/d/1aKiTutNwmsbQ9dNm15BYotKnjPUbZKUKVi2DgoaUhHs/edit)    
- Requirement Doc **Module 18.5** : [Google Doc \(Current Branch\)](https://docs.google.com/document/d/1sQFX--wDTK6DpdzJf2MDH5ovFdvSpnEtM4S0-yB98ug/edit)    

After cloning this repository, you need to initiate a virtual environment. Then install necessary packages within it.    

1. Go to project directory
```console
cd phitron-django-003-practice-01
```
Here `practice_form_fields_project` is the project folder, where the `settings.py` is the root settings file for the whole project, `urls.py` is the main url pattern handler. (CEO Shaheb 😉)    


2. Run the command given below to create a virtual environment within the .venv directory
```console
# For Linux/MacOS
python3 -m venv .venv
```

```console
# For Windows
python -m venv .venv
```
**You need to do this once, after cloning the project. .venv folder is ignored within .gitignore file**    


3. Now run the command below to activate the virtual environment.
```console
# For Linux/MacOS
source .venv/bin/activate
```

```console
# For Windows
.\.venv\Scripts\activate
```


4. Now run this once to install all the packages
```console
pip install -r requirements.txt
```


5. You are good to go. To start the development server, simply run
```console
python manage.py runserver
```
**Make sure you are within the right directory by entering `ls` or `dir` command to check if manage.py exists**    


