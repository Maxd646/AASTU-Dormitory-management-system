AASTU Dormitory Management System 🏢
A web-based dormitory management platform built using Django. This system helps AASTU dorm staff and proctors efficiently manage dormitory records, student allocations, reporting, and communication.

🚀 Features

🧑‍💼 Separate Admin Panels:
  - Proctor Panel: Student assignments, approvals, notifications
  - Staff Panel: Room management, bed availability, maintenance tracking
📋 Student Information Management
🛏️ Bed and Room Allocation System
📊 Report Generation
🔐 Authentication using Django-Allauth
🎨 Custom HTML templates: Home, Index, and Report pages
🌐 Responsive front-end (HTML/CSS/Bootstrap)

📁 Project Structure
Dorm_management_system/
├── core/                  # Django core settings and URLs
├── templates/             # HTML templates (home, index, report)
├── staticfiles/           # Static assets
├── manage.py              # Django's CLI utility
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

🛠️ Tech Stack
- Backend: Django 5.2.1
- Frontend: HTML5, Bootstrap
- Auth: Django-Allauth
- Database: SQLite3 (default)
- Deployment Ready: Gunicorn + Whitenoise

⚙️ Installation
1. Clone the Repository
   git clone https://github.com/Maxd646/AASTU-Dormitory-management-system.git
   cd Dorm_management_system

2. Set Up Virtual Environment
   python -m venv .venv
   .\.venv\Scripts\activate

3. Install Dependencies
   pip install -r requirements.txt

4. Run the Server
   python manage.py runserver 8001

5. Access the App
   Open your browser and go to: http://127.0.0.1:8001

🧪 Testing Accounts
Proctor:
  - Username: proctor
  - Password: yourpassword

Staff:
  - Username: staff
  - Password: yourpassword

(⚠️ Replace with real or dummy credentials before sharing)

📌 Future Improvements
- Student self-registration and requests
- Notifications via email or SMS
- Admin analytics dashboard
- Mobile responsiveness enhancements

🙌 Contribution
Contributions are welcome! Feel free to open issues or submit pull requests.
📄 License
This project is licensed under the MIT License.

Made with ❤️ by Team 6 – AASTU, Software Engineering Department
