def calculate_grade(line):
    line = line[:-1]
    data = line.split(":")
    
    student_name = data[0]
    grades = data[1].split(",")
    
    midterm1 = int(grades[0])
    midterm2 = int(grades[1])
    final = int(grades[2])

    average = int(((midterm1 + midterm2) / 2) * 0.40) + int(final * 0.60)

    if average >= 90:
        letter_grade = "AA"
    elif average >= 85:
        letter_grade = "BA"
    elif average >= 80:
        letter_grade = "BB"
    elif average >= 75:
        letter_grade = "CB"
    elif average >= 70:
        letter_grade = "CC"
    elif average >= 65:
        letter_grade = "DC"
    elif average >= 60:
        letter_grade = "DD"
    elif average >= 50:
        letter_grade = "DF"
    else:
        letter_grade = "FF"

    return student_name + ":" + letter_grade + "\n"

def read_grades():
    with open("exam_scores.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(calculate_grade(line))

def add_grade():
    student_name = input("Öğrenci Adı: ")
    student_surname = input("Öğrenci Soyadı: ")
    midterm1 = input("Vize 1: ")
    midterm2 = input("Vize 2: ")
    final = input("Final: ")
    
    with open("exam_scores.txt", "a", encoding="utf-8") as file:
        file.write(student_name + " " + student_surname + ":" + midterm1 + "," + midterm2 + "," + final + "\n")

def save_grades():
    with open("exam_scores.txt", "r", encoding="utf-8") as file:
        grades_list = []

        for line in file:
            grades_list.append(calculate_grade(line))

        with open("results.txt", "w", encoding="utf-8") as file2:
            for grade in grades_list:
                file2.write(grade)

def main_menu():
    while True:
        operation = input("1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış\n")

        if operation == "1":
            read_grades()
        elif operation == "2":
            add_grade()
        elif operation == "3":
            save_grades()
        elif operation == "4":
            print("Uygulamadan çıkılıyor.")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main_menu()
