def average_temperature():
    days_qt = int(input("How many day's temperature?"))

    days_temperatures = [0] * days_qt
    average = 0
    days_above_average = 0

    for i in range(days_qt):
        day_temp = float(input("Day {0}'s high temp: ".format(i + 1)))

        days_temperatures[i] = day_temp

    average = sum(days_temperatures) / days_qt
    for day_temp in days_temperatures:
        if day_temp > average:
            days_above_average += 1

    print(f"Average = {average}")
    print(f"{days_above_average} day(s) above average")


if __name__ == "__main__":
    average_temperature()
