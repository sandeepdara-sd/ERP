# 🚀 ERP System (Django-Based)

## 📌 Overview
This is a **full-fledged ERP (Enterprise Resource Planning) system** built using **Python, Django, HTML, and CSS**. The system streamlines organizational processes by managing various business functionalities like user management, inventory, and product handling.

## ✨ Features
- 🔐 User authentication and role-based access control
- 🛆 Product and inventory management
- ⚙️ Django admin panel for easy backend operations
- 🔒 Secure and scalable database using SQLite
- 🖼️ Media storage for product images
- 🏢 Modular and maintainable code structure

## 🛠 Technologies Used
### 🖙 Backend
- 🐍 **Python** - Core programming language
- 🌍 **Django** - Web framework for backend development
- 🐄 **SQLite** - Lightweight database for storing ERP data

### 🎨 Frontend
- 📝 **HTML** - Structure of web pages
- 🎨 **CSS** - Styling for an interactive UI
- 🍿 **Django Templates** - Dynamic content rendering

## 👅 Live Demo
🔗 **[ERP System Live](https://your-deployment-link.com)**

## 👥 User Roles
- **Admin**: Full access to manage users, products, and inventory
- **Manager**: Limited access to inventory and reports
- **Employee**: Can update product details

## 👅 Installation
### ✅ Prerequisites
Ensure you have the following installed:
- 🐍 Python (>=3.8)
- 📺 pip (Python package manager)
- 📂 Virtual environment (optional but recommended)

### 🔧 Steps to Run Locally
#### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/erp-system.git
cd erp-system
```

#### 2️⃣ Create and Activate a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

#### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

#### 4️⃣ Apply Migrations and Start the Server
```sh
python manage.py migrate
python manage.py runserver
```

#### 5️⃣ Access the Application
Open your browser and go to: 
```
http://127.0.0.1:8000/
```

## 📂 Folder Structure
```
erp-system/
├── 💾 .idea/                  # IDE-related files
├── 🔬 erpproject/             # Main Django project folder
│   ├── 📁 __pycache__/
│   ├── 📝 __init__.py
│   ├── ⚙️ asgi.py
│   ├── ⚙️ settings.py
│   ├── 🔗 urls.py
│   ├── ⚙️ wsgi.py
│   ├── 👀 views.py
│
├── 🔬 erpapp/                 # Core ERP application
│   ├── 📁 __pycache__/
│   ├── 📁 migrations/
│   ├── 📝 __init__.py
│   ├── 🌐 admin.py
│   ├── ⚙️ apps.py
│   ├── 📜 forms.py
│   ├── 🏗️ models.py
│   ├── 🛠️ tests.py
│   ├── 🔗 urls.py
│   ├── 👀 views.py
│
├── 🖼️ media/productimages/    # Stores product images
├── 🎨 static/                 # Static assets (CSS, JS, images)
├── 🌆 templates/              # HTML templates
├── 💾 db.sqlite3              # SQLite database
├── ⚙️ manage.py               # Django management script
├── 📖 README.md               # Project documentation
```

## 🚀 Future Enhancements
- 📊 Implement advanced analytics and reporting
- 📢 Add real-time notifications
- 💳 Integrate payment gateway for seamless transactions
- 🌈 Improve UI/UX with modern frameworks like React

## 📚 License
This project is open-source and available under the **MIT License**.

## 👨‍💻 Author
**Sandeep Dara**  
🔗 [GitHub](https://github.com/sandeepdara-sd)  
🔗 [LinkedIn](https://linkedin.com/in/sandeep-dara-1b0a23242)

