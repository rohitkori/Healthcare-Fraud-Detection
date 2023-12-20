# Healthcare Fraud Detection

<img src="./static/img/healthcare-fraud-detection-cover.png"/>

## Steps to run the project

- Clone the repository using the command

```bash
git clone https://github.com/rohitkori/Healthcare-Fraud-Detection.git
```

- Enter the virtual environment using the command

```bash
pipenv shell
```

- Install the dependencies using the command

```bash
pipenv install
```

- Run the command

```bash
python manage.py migrate
```

to migrate the database

- Run the command

```bash
python manage.py runserver
```

The backend will be served at [localhost:8000](http://localhost:8000/)

## Docker

- If you have docker installed on your system, you can run the project using the command

```bash
docker-compose up
```
