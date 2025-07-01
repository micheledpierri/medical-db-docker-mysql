<p align="left">
  <img src="https://www.vectorlogo.zone/logos/python/python-icon.svg" alt="Python" width="40"/>
  <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="Flask" width="40"/>
  <img src="https://www.vectorlogo.zone/logos/docker/docker-icon.svg" alt="Docker" width="40"/>
  <img src="https://www.vectorlogo.zone/logos/mysql/mysql-icon.svg" alt="MySQL" width="40"/>
  <img src="https://www.vectorlogo.zone/logos/sqlalchemy/sqlalchemy-icon.svg" alt="SQLAlchemy" width="40"/>
</p>

![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.3-lightgrey)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-2.0-orange)
![MySQL](https://img.shields.io/badge/mysql-%234479A1.svg?logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-20.10-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


# Medical Database with Docker, Flask, SQLAlchemy and MySQL

This repository provides a minimal working example of a medical database web app using Docker, Flask, SQLAlchemy, and MySQL.

- **Related blog post:** [Create a medical database with Docker](https://www.micheledpierri.com/2025/07/01/create-a-medical-database-with-docker/)

## Quick start

1. Clone the repository:
    ```
    git clone https://github.com/TUO_USERNAME/medical-db-docker-mysql.git
    cd medical-db-docker-mysql
    ```
2. Install requirements (if running locally):
    ```
    pip install -r requirements.txt
    ```
3. Start the project with Docker:
    ```
    docker-compose up --build
    ```
4. Access the app in your browser (usually at [http://localhost:5000](http://localhost:5000))

## Project structure

- `app/`: Python source code
- `templates/`: HTML templates
- `docker-compose.yml`: Docker config
- `requirements.txt`: Python dependencies

## License

MIT

---

Feel free to improve or extend this project!
