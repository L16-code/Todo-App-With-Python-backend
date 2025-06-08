# 🚀 Sanic Backend Boilerplate

A lightweight, high-performance API boilerplate built with the Sanic framework.

## 📖 About

This boilerplate provides a minimal setup for creating a REST API using the [Sanic](https://sanic.dev/en/) framework. Sanic is an async Python web server that's built to be fast, simple, and easy to use.

Sanic allows for asynchronous request handling, making it ideal for I/O-bound applications that require high throughput.

**Documentation**: [https://sanic.dev/en/#production-ready](https://sanic.dev/en/#production-ready)

## ✨ Features

- Asynchronous request handling
- Simple CRUD API structure
- CORS middleware configuration
- Easy to extend and customize
- Minimal dependencies
- Type hints and modern Python practices

## 🛠️ Tech Stack

- [Python](https://www.python.org/) - Programming language
- [Sanic](https://sanic.dev/en/) - Web framework
- [Sanic-CORS](https://github.com/ashleysommer/sanic-cors) - CORS handling

### Prerequisites

- Python 3.7.10
- pip (Python package manager)

## 🚦 Getting Started

### Environment Setup

You can use any of the following methods to set up your environment:

#### Using venv (Python's built-in virtual environment)

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

#### Using conda

```bash
# Create a conda environment
conda create -n sanic-boilerplate python=3.9

# Activate the environment
conda activate sanic-boilerplate
```

### Installing Requirements

Install the dependencies using pip:

```bash
pip install -r requirements.txt
```

### Managing Requirements

1. To add new requirements:
   - Add the package name to `requirements.txt`
   - Run `pip install -r requirements.txt`

2. Alternatively, install directly and update requirements:
   ```bash
   pip install package-name
   pip freeze > requirements.txt
   ```

### Running the Server

```bash
python main.py
```

The server will start on `http://localhost:8000`.

## 📁 Project Structure

```
sanic-boilerplate/
├── main.py          # Main application file with route definitions
├── db_setup.py      # Database initialization script (SQLite)
├── todos.db         # SQLite database (created after running db_setup.py)
├── requirements.txt # Project dependencies
└── README.md        # Project documentation

```

### Endpoints

- `GET /ping` - Health check endpoint
- `GET /api/items` - Get all items
- `POST /api/items` - Create a new item
- `PUT /api/items/:id` - Update an item
- `DELETE /api/items/:id` - Delete an item

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 🆘 Support

If you have any questions or run into issues, please:

1. Check the [Sanic documentation](https://sanic.dev/en/guide/)
2. Open an issue in this repository

---
## Database Setup
python db_setup.py


**Happy coding!** 🎉 
