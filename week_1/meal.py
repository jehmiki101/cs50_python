''''
breakfast 7:00-8:00
lunch 12:00-13:00
dinner 18:00-19:00

calculo de hora: 1:50
(50 / 60) + 1

.split(":")
'''

def main():
    time_input = input("What time is it? ")
    hour = convert(time_input)
    if 7 <= hour <= 8:
        print("breakfast time")
    elif 12 <= hour <= 13:
        print("lunch time")
    elif 18 <= hour <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    time_float_hour = float(hours)
    time_float_min = float(minutes) / 60
    return time_float_hour + time_float_min


if __name__ == "__main__":
    main()
