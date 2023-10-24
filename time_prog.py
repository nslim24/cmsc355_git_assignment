def hours(mins):
    hours = float(mins)/60.0
    return hours

if __name__ == "__main__":
    mins = 150
    print("For", mins, "minutes, there are", hours(mins), "hours." )

