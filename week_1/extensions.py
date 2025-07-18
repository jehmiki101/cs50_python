def main():
    text = input("File name: ")
    if ".gif" in text:
        print("image/gif")
    elif ".jpg" in text:
        print("image/jpg")
    elif ".jpeg":
        print("image/jpeg")
    elif "png":
        print("image/png")
    elif "pdf":
        print("application/pdf")
    elif "txt":
        print("text/plain")
    elif "zip":
        print("application/zip")
    else:
        print("application/octet-stream")
main()