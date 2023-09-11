from datetime import datetime
import sys
def main():
    
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)

if __name__ == "__main__":
    main()