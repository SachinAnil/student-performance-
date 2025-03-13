# 🎓 Student Performance Predictor

This project is a **Machine Learning-based web application** that predicts a student's **total score** based on their performance in Math, Reading, and Writing. Built with Python, Flask, and scikit-learn, the app provides a simple interface for educators or institutions to estimate overall student outcomes from individual subject scores.

![App Screenshot](https://github.com/SachinAnil/student-performance-/blob/main/screenshot.png)

---

## 🔍 Project Overview

**Purpose:**  
To develop a smart prediction system that uses historical student performance data to predict total scores with high accuracy.

**Key Features:**
- Predicts total score from Math, Reading, and Writing inputs
- Built-in Linear Regression model
- Responsive web interface using HTML & CSS
- Background image and centered layout for enhanced UI/UX
- Model saved using `pickle` for reuse without retraining

---

## 🚀 Tech Stack

- **Frontend:** HTML, CSS
- **Backend:** Python, Flask
- **Machine Learning:** scikit-learn, pandas
- **IDE:** Visual Studio Code

---

## 📁 Dataset

The model is trained using a student performance dataset consisting of the following features:
- `math_score`
- `reading_score`
- `writing_score`
- Additional attributes like gender, parental education, lunch, etc.

---

## 🧠 Model

The model uses a **Linear Regression** algorithm to learn the correlation between subject scores and total performance. After training, the model is serialized using `pickle` and served via Flask.

---

## 🛠 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/SachinAnil/student-performance-.git
   cd student-performance-
🧑‍💻 About Me
I’m Sachin Anil Krishna Kummara, a passionate MCA graduate with a strong foundation in Python, Java, SQL, and Data Structures & Algorithms.
📫 anilsachin52@gmail.com
🔗 LinkedIn

Highlights:
Built various tech projects including a personal portfolio, a blockchain fee payment system, and a crop disease identifier using ML.
Skilled in Flask, React.js, MySQL, Bootstrap, and OpenCV.
Leadership experience in coding clubs and hackathon management.

📌 Future Enhancements
Include additional features like study_hours, attendance, assignment_score
Support grade prediction as classification
Deploy app on cloud (Heroku/Render/AWS)
User authentication and dashboard for teachers
