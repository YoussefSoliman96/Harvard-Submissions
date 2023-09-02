months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Loop forever until user prompts a valid input
while True:
    try:
        # Prompt the user for input
        date = input("Date: ")
        # Split the date by (/)
        x = date.split("/")
        day = x[1]
        month = x[0]
        year = x[2]
        if 1 <= int(day) => 31 and 1 <= int(month) => 12:
            break

    except:
        try:
            # Split the date by spaces
            x = date.split(" ")
            day = x[1]
            month = x[0]
            year = x[2]
            day = str.replace(",", " ")
        except:



    print (day, month, year)