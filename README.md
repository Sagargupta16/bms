# BMS (Student Management System)

BMS stands for Batch Management System -- it manages the student records of a college batch.

A modern, FastAPI-based web application for managing student data with authentication, profile management, and social/coding platform integration. Built with MongoDB for robust data storage and RESTful API design.

## 🚀 Features

- **Student Authentication** - Secure sign-up and sign-in functionality
- **Profile Management** - Complete CRUD operations for student profiles
- **Social Integration** - Support for Instagram, LinkedIn, GitHub, and personal websites
- **Coding Profiles** - Integration with competitive programming platforms (LeetCode, HackerRank, CodeChef, Codeforces, GeeksforGeeks)
- **Data Validation** - Robust input validation using Pydantic models
- **RESTful API** - Clean, documented API endpoints

## 🛠️ Tech Stack

- **Backend**: Python 3.11+, FastAPI
- **Database**: MongoDB (with PyMongo)
- **Validation**: Pydantic
- **Server**: Uvicorn (ASGI)
- **Configuration**: YAML support

## 📁 Project Structure

```text
BMS/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── config/
│   └── secrets_parser.py   # Database configuration
├── models/
│   └── student_model.py    # Pydantic data models
├── routes/
│   └── student_routes.py   # API route definitions
└── services/
    ├── auth_service.py     # Authentication logic
    └── student_service.py  # Business logic
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- MongoDB instance (local or cloud)
- Git

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Sagargupta16/BMS.git
   cd BMS
   ```

2. **Set up virtual environment**

   ```bash
   pip install virtualenv
   virtualenv venv
   venv\Scripts\Activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database**
   - Copy `config/secrets.yml.example` to `config/secrets.yml`
   - Fill in your MongoDB `host`, `port`, `database`, and `connection_string`
   - Ensure MongoDB is running and accessible

5. **Run the application**

   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`

### Development Setup

To deactivate the virtual environment:

```bash
deactivate
```

## 📚 API Documentation

Once the application is running, visit:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/students/` | List all students |
| GET | `/students/{student_id}` | Get student by ID |
| POST | `/students/sign-up` | Register new student |
| POST | `/students/sign-in` | Authenticate student |
| PUT | `/students/{student_id}` | Update student profile |
| PUT | `/students/{student_id}/password` | Update student password |
| PUT | `/students/{student_id}/socials` | Update social profiles |
| PUT | `/students/{student_id}/coding` | Update coding profiles |
| DELETE | `/students/{student_id}` | Delete student |

### Student Model

Students have the following profile structure:

```json
{
  "student_id": 12345,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@student.nitw.ac.in",
  "personal_email": "john.doe@gmail.com",
  "socials": {
    "instagram": "john_doe",
    "linkedin": "john-doe",
    "github": "johndoe",
    "website": "https://johndoe.dev"
  },
  "coding": {
    "Leetcode": "johndoe",
    "Hackerrank": "johndoe",
    "Codechef": "johndoe",
    "Codeforces": "johndoe",
    "GFG": "johndoe"
  },
  "date_of_birth": "2000-01-01T00:00:00",
  "year": 3
}
```

## 🔧 Configuration

Update the following files for your environment:

- `config/secrets.yml` - Database connection settings (copy from `config/secrets.yml.example`)
- `requirements.txt` - Add any additional dependencies

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Sagar Gupta** - [@Sagargupta16](https://github.com/Sagargupta16)

## 🙏 Acknowledgments

- FastAPI community for excellent documentation
- MongoDB for reliable database solutions
- Python community for amazing libraries

