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
        x = str.split(date, "/")
        day = x[1]
        month = x[0]
        year = x[2]
        if 1 <= day => 31 and 1 <= month => 12:


    except:
        try:
            # Split the date by spaces
            x = str.split(date, " ")
            day = x[1]
            month = x[0]
            year = x[2]
            day = replace(",", " ")
        except:



    print (day, month, year)