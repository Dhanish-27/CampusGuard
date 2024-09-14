CampusGuard
CampusGuard is a Django-based application designed to track and identify whether hostel students are currently on campus or off campus. This tool helps hostel management and staff monitor student presence and ensure campus safety and compliance.

Features
Real-time Tracking: Monitor students' presence on campus in real time.
Student Management: Add, update, and remove student records.
Presence Logs: View logs of students' entry and exit times.
Alerts: Receive notifications for specific events or status changes.
Installation
Prerequisites
Python 3.8 or higher
Django 4.0 or higher
Steps to Install
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/campusguard.git
cd campusguard
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Create a superuser (for admin access):

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Access the application:

Open your web browser and go to http://127.0.0.1:8000 to start using CampusGuard.

Usage
Admin Panel: Access the Django admin panel at http://127.0.0.1:8000/admin to manage students and view presence logs.
Student Dashboard: Students can check their status and presence logs through the student dashboard.
Configuration
You may need to configure settings such as the database connection, email settings, and other application-specific settings. Edit settings.py to update these configurations.

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/your-feature).
Create a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or issues, please contact:

Author: Your Name
Email: your.email@example.com
GitHub: yourusername
