# Script to download free files released by Springer

import requests, wget, os
import pandas as pd

# check if the books folder exists
# if not create one
def createBooksFolder():
    try:
        if not os.path.isdir(os.path.join(os.getcwd(), "books")):
            os.mkdir(os.path.join(os.getcwd(), "books"))
    except OSError as e:
        print("Unable to create file\n{}".format(e))

def main():
    # Pandas read the excel file
    df = pd.read_excel("Free+English+textbooks.xlsx")
    
    # check if the books folder exists if not create one
    createBooksFolder()
    
    # Download the files one by one
    for index, row in df.iterrows():
            # loop through the excel list
            file_name = f"{row.loc['Book Title']}{row.loc['Edition']}".replace('/','-').replace(':','-')
            url = f"{row.loc['OpenURL']}"
            r = requests.get(url) 
            download_url = f"{r.url.replace('book','content/pdf')}.pdf"
            wget.download(download_url, f"./books/{file_name}.pdf") 
            print(f"downloading {file_name}.pdf Complete ....")

if __name__ == "__main__":
    main()