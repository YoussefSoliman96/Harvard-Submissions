x = input("Filename: ").lower().strip()
print(x)
if ".gif" in x:
    print("images/gif")
elif ".jpg" in x:
    print("images/jpg")
elif ".jpeg" in x:
    print("images/jpeg")
elif ".png" in x:
    print("images/png")
elif ".pdf" in x:
    print("application/pdf")
elif ".txt" in x:
    print("text/txt")
elif ".zip" in x:
    print("application/zip")

else:
    print("application/octet-stream")