# First Django Blog
This is a simple Django blog

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

You need to preinstalled Python3.6 or up. See Python's website how to install it.  
 
 
### Installing

This guide is only provided for unix. In windows it's your responsibility to run the project.

A step by step series of examples that tell you how to get a development env running.

Open terminal where you want to clone this project.

Clone the repo
```
git clone https://github.com/codewithrakib/first-django-blog.git
```

Select the directory
```
cd first-django-blog
```

Create Python virtual env
```
python3 -m venv venv
```

Activate virtual env
```
source venv/bin/activate
```

Upgrade pip
```
pip install --upgrade pip
```

Install dependencies from requirements.txt
```
pip install -r requirements.txt
```


Go to ```src/``` directory
```
cd src
```

Migrate the database
```
python manage.py migrate
```

Create Super User. After giving this command it will prompt for username, password, email etc. Give this as you want.
```
python manage.py createsuperuser
```

Start the development server
```
python manage.py runserver
```

Open this link http://127.0.0.1:8000/ on your browser. Perhaps you need a network connection for nice UI because of Bootstrap CDN. Enjoy the app and if you find any bug just contribute our project. Just always remember to keep only predownloaded files inside ```static_cdn_test/``` and ```src/staticfiles/``` direcotries before you push your code.


## Running the tests

This project has no testing included

## Built With

* Django
* Python
* HTML
* CSS
* Bootstrap4

## Contributing

You are always welcome to contribute it. You may add tests, separate frontend, fixing ui, add messaging service etc. Just always remember to keep only predownloaded files inside ```static_cdn_test/``` and ```src/staticfiles/``` direcotries before you push your code.


## Authors

* **Md Rakibul Hasan** - *Initial work* - [rhasancodes](https://github.com/rhasancodes)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

