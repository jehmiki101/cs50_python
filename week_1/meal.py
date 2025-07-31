''''
breakfast 7:00-8:00
lunch 12:00-13:00
dinner 18:00-19:00

calculo de hora: 1:50
(50 / 60) + 1

.split(":")
'''

def main():
    time_input = input("What time is it? ").split(":")
    if 7 < convert(time_input) < 8:
        print("breakfast time")
    elif 12 < convert(time_input) < 13:
        print("lunch time")
    if 18 < convert(time_input) < 19:
        print("dinner time")


def convert(time):
    time_float_hour = float(time[0])
    time_float_min = float(time[1])
    hour_to_number = (time_float_min / 60) + time_float_hour
    return hour_to_number

    
if __name__ == "__main__":
    main()