# Hexagonal Architecture Archetype with FastAPI

This project provides an archetype for implementing a Hexagonal Architecture using FastAPI. It serves as a template for building scalable and maintainable web applications by adhering to the principles of Hexagonal Architecture, also known as Ports and Adapters architecture.

## Project Structure

The project is organized into several key modules:

1. **Domain**: Contains the core business logic, including use cases and domain models. This layer is independent of external frameworks and libraries.

2. **Application**: This layer orchestrates the business logic by handling use cases and managing the flow of data between the domain and infrastructure layers. It includes handlers and application-level services.

3. **Driven adapters**: Manages the interaction with external systems, such as databases, external APIs, and other services. This layer includes data persistence, API clients, and other integrations.

4. **Entry Points**: The external interface of the application, including API endpoints defined using FastAPI. This layer handles HTTP requests and responses, interacting with the application layer to process business logic.

## Key Features

- **FastAPI Integration**: Utilizes FastAPI for creating robust and efficient APIs, benefiting from its automatic generation of OpenAPI and JSON schema documentation.

- **Dependency Injection**: Implements the `dependency_injector` library to manage dependencies, ensuring loose coupling between components and enhancing testability.

- **Custom Exception Handling**: Provides a structured approach for handling custom exceptions and error responses, improving the consistency and readability of the API.

- **Data Transfer Objects (DTOs)**: Uses DTOs for structured data exchange between the client and the server, ensuring that only the necessary information is exposed.

## How to Use

1. **Setup**: Clone the repository and set up a virtual environment. Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

2. **Running the Application**: Start the FastAPI application using Uvicorn:

   ```bash
    uvicorn app.main:app --reload
   ```
3. **API Documentation**: Access the interactive API documentation at `http://127.0.0.1:8000/docs` for the OpenAPI interface, or at `http://127.0.0.1:8000/redoc` for the ReDoc interface. These endpoints provide a detailed view of the available API endpoints, request/response schemas, and other useful information.

4. **Extending the Archetype**: The provided structure can be extended by adding new use cases, domain models, infrastructure services, and API endpoints as needed. The modular architecture makes it easy to add new functionality or modify existing components without affecting other parts of the system.

## Contributing

Contributions are welcome! If you have ideas for improving this archetype or find any issues, please feel free to submit a pull request or open an issue. We appreciate any feedback or suggestions to enhance the functionality and usability of this template.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This archetype aims to streamline the development process by providing a well-structured foundation based on Hexagonal Architecture principles. It is designed to be adaptable to various types of projects and requirements, ensuring a clean separation of concerns and ease of maintenance.
