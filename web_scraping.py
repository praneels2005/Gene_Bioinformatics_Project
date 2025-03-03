# Create a virtual environment: python3 -m venv venv_name
# activate virtual environment: source venv/bin/activate

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selectorlib import Extractor
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import UnexpectedAlertPresentException
import requests
import json
import time
from bs4 import BeautifulSoup
#mpi4py
#Personal Library
import GenManLib
from GenManLib import myfunctions


from selenium.webdriver.firefox.options import Options
from pymongo import MongoClient

#Step 3
def upload(Protein, data):
    client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongodb-vscode+1.10.0")
    
    db = client.Proteins
    
    with open(data, 'r') as file:
        upload_data = json.load(file)
    
    db.create_collection(Protein)
    db[Protein].insert_many(upload_data)
    
    
#Step 4  
#Call Manipulations each time client would like to view gene sequence manipulations
def Manipulations(Protein,Strain):
    client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongodb-vscode+1.10.0")
    
    db = client.Proteins
    
    collection = db[Protein]
    
    #Returns a single document's gene sequence
    result = collection.find_one({"Name": Strain}, {"_id":False, "Sequence": True})
    
    Sequence = str(result["Sequence"])
    print("Original Sequence:\n",Sequence)
    #print("\nComplement of Sequence:\n",myfunctions.complement(Sequence))
    #print("\nReverse of Sequence:\n",myfunctions.reverse(Sequence))
    #print("\nTranslation:\n",myfunctions.Translation(Sequence))
    #Translated_Sequence=myfunctions.Translation(Sequence)
    #print("\nBack-Translation:\n",myfunctions.Back_Translation(Translated_Sequence))
    #print("GC-Content Calculation:",myfunctions.GC_Content(Sequence))
    #print("K-MERS w/ k = 3:",myfunctions.K_MER(Sequence,3))


    
#Step 2    
def Extract_Genetic_Sequences(Protein, data):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    
    with open(data, "r") as file:
        URLS = json.load(file)
        
            
    Name_Sequence= []
    for item in URLS:
        driver.get(item["URL"])
        driver.implicitly_wait(60)
        #join elimnates spacing
        #splitlines() splits the text into a list of lines
        #[1:] skips the first line and keeps the rest
        #Use ""(double-quotations) to access tag elements
        body = "\n".join((driver.find_element(By.TAG_NAME, "pre").text).splitlines()[1:])
        
        Name_Sequence.append({
                    "Name": item["Sequence Name"],
                    "Sequence": body
                })
    file_name = Protein+"_Strains"
    with open(file_name, "w") as outfile:
        json.dump(Name_Sequence, outfile, indent = 4)
        
    upload(Protein, file_name)
    #upload(Protein,json.load(outfile)) 
    
    
#Step 1
def Scrape(Protein,Database_Option):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    driver.get("https://www.ncbi.nlm.nih.gov")
    driver.implicitly_wait(30)

    search_box = driver.find_element(By.ID,'term').send_keys(Protein)

    #locate dropdown
    Database = driver.find_element(By.ID, 'database')
    
    #Open the dropdown and select the requested database
    dropdown = Select(Database)
    dropdown.select_by_visible_text(Database_Option)

    search_box = driver.find_element(By.ID,'search').click()
    driver.implicitly_wait(30)
    
    num_page = driver.find_element(By.CLASS_NAME, 'num').get_attribute('last')
    #print(num_page)
    
    
    URLS = []
    for i in range(int(num_page)-1):
        page_ = i+1
        
        #Strain name
        Results = driver.find_elements(By.CLASS_NAME, 'rslt')
        
        #Fasta link
        FASTAS = driver.find_elements(By.ID, 'ReportShortCut6')
        urls = [link.get_attribute('href') for link in FASTAS]
        print(f"\nExtracted strains of",Protein,"from page",str(page_))
        
        #Two elements simulatensouly traverse through their respective lists
        page_index = 0
        for url,name in zip(urls, Results):
            URLS.append({
                    "Page:": page_,
                    "Index: ": page_index,
                    "Sequence Name": name.find_element(By.CLASS_NAME, 'title').text,
                    "URL": url
                })
            page_index +=1
        driver.implicitly_wait(4)
        
        #Exception is thrown at the last page and driver clicks on next page button
        try:
            click_next = driver.find_element(By.CLASS_NAME, 'active.page_link.next').click()
        except:
            print("\nEnd of pages")
            break
    
    file_name = "FASTA_URLS_"+Protein+".json"
    #Dumps all FASTA URLS and strain names into json file
    with open(file_name, "w") as outfile:
        json.dump(URLS, outfile, indent = 4)
        
    Extract_Genetic_Sequences(Protein, file_name)
        

start = time.time()
Scrape("HSP105","Nucleotide")   
#upload("HSP105", "HSP105_Strains")
end = time.time()
length = end-start
print("Total Time: ",length)    
    
'''
Step 1:
Run Scrape(Protein, Database_Option)
Output File Name: FASTA_URLS_<Protein_Name>

Step 2:
Extract gene sequences from FASTA URL json using Extract_Genetic_Sequences(Protein, FASTA_URLS_<Protein_Name>)
Output File Name: <Protein_Name>_Strains

Step 3:
Upload Strains Json file to database upload(Protein, <Protein>_Strains)
'''    
    
#Scrape("HSP104", "Nucleotide")

#Extract_Genetic_Sequences("HSP104")

#Manipulations("HSP104", "Brettanomyces bruxellensis genome assembly, contig: scaffold1, whole genome shotgun sequence")

#with open("testing.json", 'r') as file:
#    data = json.load(file)
#upload("Test_Protein", data)


