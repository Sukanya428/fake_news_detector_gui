import tkinter as tk
from tkinter import messagebox
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# GUI window
window = tk.Tk()
window.title("Fake News Detector")
window.geometry("500x300")

label = tk.Label(window, text="Enter News Article:", font=("Arial", 14))
label.pack(pady=10)

text_input = tk.Text(window, height=10, width=50)
text_input.pack(pady=10)

def check_news():
    news = text_input.get("1.0", tk.END)
    transformed = vectorizer.transform([news])
    result = model.predict(transformed)
    message = "FAKE NEWS" if result[0] == 0 else "REAL NEWS"
    messagebox.showinfo("Prediction", f"The article is: {message}")

button = tk.Button(window, text="Check", command=check_news)
button.pack(pady=10)

window.mainloop()