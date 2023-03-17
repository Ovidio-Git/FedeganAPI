# FedeganAPI

This API provides access to data from the Colombian agricultural industry, sourced from the Fedegan website. It is built with FastAPI, uses PostgreSQL for data storage, and is containerized with Docker. Unit testing is included for added reliability, and CI/CD is handled with GitHub Actions.

## Setup

### Requirements

- Docker
- Docker Compose

### Instructions

1. Clone this repository to your local machine.
2. Create a .env file at the root of the project, and add the following environment variables:

```sh
SERCRET_KEY=<your_secret_key>
```

3. In your terminal, navigate to the project directory and run:

```sh
docker-compose up --build
```

4. Once the containers are up and running, you can access the API at `http://localhost:3000/docs`.

## Usage

### Authorization

To access protected endpoints, include the access token in the header `Authorization` of the request. The header should be in the format `Bearer <access_token>`.

This API uses JWT authentication. To authenticate, send a POST request to `/api/token/` with a JSON payload containing `username` and `password` fields.

### User Registration

To register a new user, send a POST request to `/api/registrarUser/` with a JSON payload.

## Testing

To run unit tests, navigate to the project directory in your terminal and run pytest.

## CI/CD

This project is set up with GitHub Actions to automatically build and deploy the Docker container to a remote server whenever changes are pushed to the main branch. The workflow also runs unit tests to ensure code quality and reliability.

## Contributing

Pull requests and issues are welcome! Please ensure that any code changes are accompanied by corresponding updates to the documentation and tests.
