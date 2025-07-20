# fake_news_detector_gui
A simple ML-based fake news detection app with Tkinter GUI
# Fake News Detection System using Machine Learning

This is a simple and effective Machine Learning-based GUI application that detects whether a news article is *Real* or *Fake* using Natural Language Processing (NLP) techniques.

# 🔍 Features

- Detects *Fake* or *Real* news using trained ML model.
- User-friendly *Tkinter GUI* for interaction.
- Built using *Python, **scikit-learn, and **TF-IDF Vectorization*.
- Trained on combined real and fake news datasets.

# 📁 Project Structure
Fakenews2/ ├── data/                
# Contains training datasets ├── gui.py               
# GUI script for the app ├── main.ipynb           
# Jupyter Notebook with training & evaluation ├── model.pkl             
# Saved trained model ├── vectorizer.pkl       
# Saved TF-IDF vectorizer

# ⚙ How it Works

1. News articles are vectorized using *TF-IDF*.
2. A *PassiveAggressiveClassifier* is trained to differentiate real vs fake news.
3. The model is saved and integrated with a *Tkinter GUI*.
4. User inputs an article → the model predicts and displays the result.

# 🚀 How to Run

1. Download or clone this repository.
2. Make sure all files (gui.py, model.pkl, vectorizer.pkl) are in the same folder.
3. Open your terminal or command prompt in the project directory.
4. Run the following command:

```bash
python gui.py

5. A GUI window will open. Paste any news content and check whether it's Real or Fake!


🛠 Tech Stack

Python

Tkinter (GUI)

Pandas, Numpy

Scikit-learn (TF-IDF, PassiveAggressiveClassifier)

Jupyter Notebook

👩‍💻 Author

Sukanya Rao
third Year BTech CSE (AI & ML)
Aspiring ML Engineer & Founder of Saarthya – a future-focused brand aimed at building meaningful products across industries.

[🌐 LinkedIn https://www.linkedin.com/in/sukanya-rao-940869329?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app ]
[📧 Email: srao45690@gmail.com]

📄 License

This project is open-source and available for learning and non-commercial use.

🌟 If you like this project, consider giving it a ⭐ on GitHub!

---
