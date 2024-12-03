tudent Management API
A RESTful API built using FastAPI and MongoDB for managing student records. This project allows you to perform CRUD (Create, Read, Update, Delete) operations on student data.

Features
Create new student records.
Read student records (all or specific).
Update existing student records.
Delete student records.
Prerequisites
Before running this project, ensure you have the following installed on your system:

Python 3.10+
MongoDB (Local or Atlas)
Node.js (for frontend integration, if needed)
Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/student-management-api.git
cd student-management-api
2. Set Up Environment Variables
Create a .env file in the root directory and add your MongoDB connection string:

env
Copy code
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority
3. Install Dependencies
Install Python dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
1. Start the Server
Run the FastAPI server:

bash
Copy code
uvicorn main:app --reload
The API will be accessible at http://127.0.0.1:8000.

2. Test Endpoints
You can test the endpoints using Postman, cURL, or the built-in FastAPI Swagger UI available at:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
API Endpoints
Root Endpoint
GET /
Returns a welcome message.

Response:

json
Copy code
{
    "message": "Welcome to the Student Management API"
}
