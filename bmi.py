print ("Menghitung berat badan BMI = Berat / tinggi. KG/M \n")

tinggi = float(input("Masukkan tinggi badan dengan satuan meter : "))

bmi = float(input("Masukkan BMI yang diharapkan : "))

#berat yang diperlukan
tinggi2 = bmi * (tinggi ** 2)

print(f"Berat yang diperlukan untuk mencapai BMI {bmi} adalah {tinggi2:.2f} kg.")