# 🎓 Student Result Portal

A **Flask-based Student Result Portal** that allows students to search their academic results using their **Hall Ticket Number**. The application includes an **Admin Panel** for managing student records, supports **PDF result generation**, and is served locally using the **Waitress WSGI server**.

---

## 🚀 Features

* 🔍 Search student results using Hall Ticket Number
* 👨‍💼 Admin panel to add and manage student records
* 🗄️ SQLite database integration
* 📄 Download results as PDF
* 📱 Responsive user interface
* ⚡ Local deployment using Waitress

---

## 🛠️ Technologies Used

* Python
* Flask
* SQLite
* HTML5
* CSS3
* ReportLab
* Waitress

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/annadivighnatha/student-result-portal.git
```

### 2. Navigate to the project directory

```bash
cd student-result-portal
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

Start the application using the Waitress server:

```bash
python run_server.py
```

### 5. Open the application

On the same computer:

```text
http://127.0.0.1:8080
```

To access it from another device on the same Wi-Fi network:

```text
http://<your-local-ip>:8080
```

---

## 📂 Project Structure

```text
Student-Result-Portal/
│
├── app.py
├── run_server.py
├── database.db
├── requirements.txt
├── static/
├── templates/
└── README.md
```

---

## 📖 How It Works

1. Enter the student's Hall Ticket Number.
2. Click **Search**.
3. View the student's academic result.
4. Download the result as a PDF.
5. Administrators can add and manage student records through the admin panel.

---

## 🔮 Future Enhancements

* Student authentication
* Multiple semester result support
* Result analytics dashboard
* Export results to Excel
* Cloud deployment

---

## 👨‍💻 Author

**Annadi Vighnatha**

GitHub: https://github.com/annadivighnatha

