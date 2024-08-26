import tkinter as tk

# Pencereyi oluşturuyorum
root = tk.Tk()
root.title("TUA BMI Calculator")
root.geometry("300x175")
root.config(padx=10, pady=10)

# Giriş alanları - arayüzü
label_kg = tk.Label(root, text="Enter Your Weight (kg)")
label_kg.pack()
entry_kg = tk.Entry(root)
entry_kg.pack()

label_cm = tk.Label(root, text="Enter Your Height (cm)")
label_cm.pack()
entry_cm = tk.Entry(root)
entry_cm.pack()

def bmi_calculate_button_clicked():
    try:
        # Kullanıcı girişi alıyorum
        height = entry_cm.get()
        weight = entry_kg.get()
    
        # Eğer herhangi bir giriş boşsa, uyarı mesajı gösteriyorum
        if not height or not weight:
            result_label.config(text="Please enter both weight and height.")
            return
        
        # Girişlerin geçerli olup olmadığını kontrol ediyorum
        height = float(height)
        weight = float(weight)
    
        # BMI hesaplama işlemi
        height_meters = height / 100  # Boyu metreye çeviriyorum
        bmi = weight / (height_meters ** 2)

        # BMI kategorileri
        if bmi <= 18.5:
            result_label.config(text=f"Your BMI is {bmi:.2f}. You are underweight.")
        elif 18.5 <= bmi <= 24.9:
            result_label.config(text=f"Your BMI is {bmi:.2f}. You are normal weight.")
        elif 25 <= bmi <= 29.9:
            result_label.config(text=f"Your BMI is {bmi:.2f}. You are overweight.")
        elif 30 <= bmi <= 34.9:
            result_label.config(text=f"Your BMI is {bmi:.2f}. You are obese class 1.")
        elif 35 <= bmi <= 40:
            result_label.config(text=f"Your BMI is {bmi:.2f}. You are obese class 2.")
        elif bmi > 40:
            result_label.config(text=f"Your BMI is {bmi:.2f}. You are obese class 3.")
            
    except ValueError:
        result_label.config(text="Please enter a valid number for kg or cm.")

# Hesaplama butonu
button = tk.Button(root, text="Calculate", command=bmi_calculate_button_clicked)
button.pack(pady=10)

# Sonucu görmek için
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
