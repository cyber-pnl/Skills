from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys


# Initialisez le navigateur Firefox
driver = webdriver.Firefox()

# Ouvrez la page web
driver.get('http://testphp.vulnweb.com/artists.php')
print(driver.title)
i =1
# Attendez quelques secondes pour permettre au site web de se charger

#Nom des artistes recherchés
artist_name = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[{}]/a/h3".format(i))
#Commenataires sur les artistes 
artist_comment=driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[{}]/p/a".format(i))
#liste cntenant les noms
l_name=[]
#liste contenant les commentaires 
l_comment=[]
#Chemin du fichier 
file_path = "/home/jeanbrice/Documents/SkillsIntern/data.txt"

for i in range (1,4):
    artist_name = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[{}]/a/h3".format(i))
    l_name.append(artist_name)
    artist_comment=driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[{}]/p/a".format(i))
    l_comment.append(artist_comment)

with open(file_path, "w") as file:
    # Écriture des chaînes de caractères dans le fichier
    
        for i in range (0,len(l_name)) :
          file.write("L'artiste:")
          file.write(l_name[i].text)
          file.write("a eu pour commentaires:") 
          file.write(l_comment[i].text + "\n")

time.sleep(3)
driver.quit()