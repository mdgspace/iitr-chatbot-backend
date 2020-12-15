# IITR_Chatbot_backend

## Setup
- Prerequisites:
  - Python 3
  - pip
  - default-libmysqlclient-dev

- Clone this repository.

- Set up a virtual environment.
```
python3 -m venv chatbot_env
```

- Activate the virtual environment.
```
source chatbot_env/bin/activate
```
- Navigate inside the cloned repository and install the required dependencies using the command:
```
pip install -r requirements.txt
```

- Navigate to /chatbot_backend and create a file named .env and store the following credentials inside it
```
SECRET_KEY=your-secret-key
```

- Navigate back to the base directory for the app where <span>manage.py</span> file is located and make the database migrations using following command:
```
python manage.py migrate
```
- Start the backend server:
```
python mange.py runserver
```

## API Structure
- To access all the links with their category and subcategory info:
```
http://127.0.0.1:8000/chatbot
```
- To access a specific link through its category, subcategory and name:
```
http://127.0.0.1:8000/chatbot/category/sub-category/name
```
