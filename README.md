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
