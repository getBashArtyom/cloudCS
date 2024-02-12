from tkinter import *
from tkinter import messagebox
import requests
import re

def predict_price():
    sqft_living_val = sqft_living.get()
    grade_val = grade.get()
    view_val = view.get()
    sqft_above_val = sqft_above.get()
    sqft_living15_val = sqft_living15.get()

    data = {
        "sqft_living": sqft_living_val,
        "grade": grade_val,
        "view": view_val,
        "sqft_above": sqft_above_val,
        "sqft_living15": sqft_living15_val
    }

    response = requests.post("http://localhost:8001/predict", json=data)
    predicted_price_match = re.search(r'Predicted Price: (\$\d+)', response.text)
    predicted_price = predicted_price_match.group(1)
    if response.status_code == 200:
        messagebox.showinfo("Prediction Result", f"Predicted Price: {predicted_price}")
    else:
        messagebox.showerror("Error", "Failed to get prediction")

root = Tk()
root.title("House Price Prediction")

Label(root, text="Sqft Living:").grid(row=0, column=0)
Label(root, text="Grade:").grid(row=1, column=0)
Label(root, text="View:").grid(row=2, column=0)
Label(root, text="Sqft Above:").grid(row=3, column=0)
Label(root, text="Sqft Living 15:").grid(row=4, column=0)

sqft_living = Entry(root)
grade = Entry(root)
view = Entry(root)
sqft_above = Entry(root)
sqft_living15 = Entry(root)

sqft_living.grid(row=0, column=1)
grade.grid(row=1, column=1)
view.grid(row=2, column=1)
sqft_above.grid(row=3, column=1)
sqft_living15.grid(row=4, column=1)

predict_button = Button(root, text="Predict", command=predict_price)
predict_button.grid(row=5, column=0, columnspan=2)

root.mainloop()
