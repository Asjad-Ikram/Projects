import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#For online url of Flexjobs(Uncomment on use)
'''url="https://www.flexjobs.com/remote-jobs/world/Anywhere?searchkeyword=Python%20Developer&useclocation=true"
page=requests.get(url)
soup=bs(page.content,"html.parser")
'''
#For Reading Local Html File(Uncomment on demonstration)
with open("D:\Projects\Web Scraping Program\Anywhere Jobs - Remote, Work From Home, Online, & Part Time _ FlexJobs.html","r", encoding='charmap', errors='ignore') as f:
    soup=bs(f,"html.parser")


    Title_List=[]
    Titles=soup.find_all("a",class_="sc-jv5lm6-13 fQyPIb textWrap")
    for title in Titles:
        Title_List.append(title)
        #print(title.string)
        "\n"

    Description=soup.find(id="job-table-wrapper")
    Description_list=[]
    job_text=Description.findChildren("p",class_="sc-jv5lm6-4")
    #print(job_text)
    for text in job_text:
        Description_list.append(text.get_text())
        #print(text.get_text())
        "\n"

df=pd.DataFrame(Title_List,columns=["Job_Title"])
df["Description"]=Description_list

print(df)

#df.to_csv(r"D:\Projects\Web Scraping Program\Scraped Data.csv",index=False)