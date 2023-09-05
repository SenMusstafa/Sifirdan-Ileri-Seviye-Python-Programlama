def divide_numbers():
    while True:
        try:
            x = int(input('x: '))
            y = int(input('y: '))
            result = x / y
        except ZeroDivisionError:
            print('y için 0 girilemez')
        except ValueError:
            print('x ve y için sayısal değer girmelisiniz')
        except Exception as ex:
            print('yanlış bilgi girdiniz:', ex)
        else:
            print('Sonuç:', result)
            break
        finally:
            print('try except sonlandı.')

if __name__ == "__main__":
    divide_numbers()
