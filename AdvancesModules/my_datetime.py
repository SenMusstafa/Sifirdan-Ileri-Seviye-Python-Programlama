from datetime import datetime, timedelta

def main():
    simdi = datetime.now()
    result = simdi.month

    result = simdi.ctime()
    result = simdi.strftime("%d")
    result = simdi.strftime("%y %b %a")
    print(result)

    t = "1 April 2021 hour 16:50:17"
    dt = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
    print(dt)

    birthday = datetime(1985, 4, 1, 16, 50, 17)
    print(birthday)

    result = birthday.timestamp()
    print(result)
    result = datetime.fromtimestamp(result)
    print(result)

    result = datetime.fromtimestamp(0)

    result = simdi - birthday

    result = simdi + timedelta(days=10)
    result = simdi - timedelta(days=10)
    print(result)

if __name__ == "__main__":
    main()
