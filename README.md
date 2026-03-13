# 🎮 Shop Games - Python Console Game Store

A simple **game store system** built with **Python and MySQL**, following a layered backend architecture.
This project simulates a digital store where users can create accounts, log in, browse games, and purchase them while managing stock and purchase history.

The goal of this project is to practice **backend development concepts**, **database integration**, and **clean project architecture**.

---

# 🚀 Features

### 👤 User System

* User registration
* Secure login authentication
* Password hashing using **SHA256**

### 🎮 Game Store

* Add new games
* List available games
* Game purchase system
* Automatic stock management

### 🧾 Purchase System

* Purchase registration
* User purchase tracking
* Database persistence

---

# 🧠 Architecture

The project follows a **layered architecture**, separating responsibilities:

```
shop-games
│
├── database
│   └── database.py        # MySQL connection
│
├── repositories
│   ├── usuario_repository.py
│   ├── jogo_repository.py
│   └── compra_repository.py
│
├── services
│   ├── usuario_service.py
│   └── loja_service.py
│
├── main.py                # Application entry point
│
└── README.md
```

### Layer responsibilities

**Database**

* Handles the MySQL connection.

**Repositories**

* Direct interaction with the database (SQL queries).

**Services**

* Business logic and system rules.

**Main**

* User interaction and application flow.

This structure is commonly used in **real backend applications**.

---

# 🛠 Technologies Used

* **Python 3**
* **MySQL**
* **MySQL Connector**
* **SHA256 (hashlib)**
* **Git & GitHub**

---

# 🗄 Database Structure

### Users

| Field    | Type    |
| -------- | ------- |
| id       | INT     |
| nome     | VARCHAR |
| username | VARCHAR |
| senha    | VARCHAR |

---

### Games

| Field   | Type    |
| ------- | ------- |
| id      | INT     |
| nome    | VARCHAR |
| preco   | DECIMAL |
| estoque | INT     |

---

### Purchases

| Field       | Type      |
| ----------- | --------- |
| id          | INT       |
| usuario_id  | INT       |
| jogo_id     | INT       |
| data_compra | TIMESTAMP |

---

# 🔐 Security

Passwords are **not stored in plain text**.

They are hashed using **SHA256** before being saved in the database.

Example:

```
User password → SHA256 → stored hash in database
```

---

# ⚙️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/shop-games.git
```

---

### 2️⃣ Install dependencies

```
pip install mysql-connector-python
```

---

### 3️⃣ Create the MySQL database

```
CREATE DATABASE shop_games;
```

Create the tables according to the structure above.

---

### 4️⃣ Configure database connection

Inside:

```
database/database.py
```

Update your credentials:

```python
mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="shop_games"
)
```

---

### 5️⃣ Run the application

```
python main.py
```

---

# 📚 Learning Goals

This project was built to practice:

* Python backend development
* Database design
* SQL queries
* Authentication logic
* Clean project structure
* Basic software architecture

---

# 📌 Future Improvements

Possible future improvements:

* REST API with **FastAPI**
* JWT authentication
* Admin panel
* Game search system
* Docker containerization
* Unit testing

---

# 👨‍💻 Author

**Gustavo Samuel**

Aspiring Backend Developer focused on **Python and APIs**.

GitHub:
https://github.com/GustaDev9

LinkedIn:
https://www.linkedin.com/in/gustavo-samuel-26a5553b1/

---

⭐ If you found this project interesting, consider giving it a star!
