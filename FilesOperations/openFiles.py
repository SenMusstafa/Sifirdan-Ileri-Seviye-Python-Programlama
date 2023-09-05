# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
#Kullanımı: open(dosya_adi, dosya_erişme_modu)
#dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

#"w": (write) yazma modu. => dosyayı konumda oluşturur.
# ** Dosya içeriğini siler ve yeniden ekleme yapar.

# file = open("newfile.txt","w",encoding="utf-8")
# file.write("Wesley Sneijder")
# # print(file)
# # file.close()
# file.close()
# #"a": (append) ekleme modu. => dosya konumda yoksa oluşturur.

# file = open("newfile.txt","a",encoding="utf-8")
# file.write("\nDidier Drogba")
# file.close()
#"x": (create) oluşturma modu. => dosya zaten varsa hata verir.

#"r": (read) okuma modu. => varsayılan. dosya konumda yoksa hata verir.

def file_operation(file_name, file_access_mode, content=None):
    try:
        with open(file_name, file_access_mode, encoding="utf-8") as file:
            if file_access_mode == "r":
                content = file.read()
                print(content)
            elif file_access_mode in ["w", "a", "x"]:
                file.write(content)
                if file_access_mode == "w":
                    print(f"{file_name} file created and content written.")
                elif file_access_mode == "a":
                    print(f"Data added to {file_name}.")
                elif file_access_mode == "x":
                    print(f"{file_name} file created.")
            else:
                print("Invalid file access mode. Valid modes: 'r', 'w', 'a', 'x'")
    except FileNotFoundError:
        print(f"{file_name} not found.")
    except Exception as error:
        print(f"An error occurred: {error}")

# Example usage:
file_operation("newfile.txt", "w", "Fernando Muslera\n")  # Creates the file and writes content
file_operation("newfile.txt", "a", "Emanuel Maura Icardi\n")  # Appends data to the file
file_operation("newfile2.txt", "x")  # Creates the file
file_operation("nonexistent.txt", "r")  # Reads the file (if it exists, or raises an error)
