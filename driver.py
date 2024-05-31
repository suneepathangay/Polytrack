from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pynput.keyboard import Key, Controller


class Driver:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.link="https://www.kodub.com/apps/polytrack"
        self.keyboard=Controller()
    
    def open_tracks(self):
        try:
            self.driver.get(self.link)
            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
            )
            
            self.driver.switch_to.frame(iframe)
            
            div_id = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'ui'))
            )
            
            menu_class=div_id.find_element(By.CLASS_NAME,"menu")
            button_classes=menu_class.find_elements(By.TAG_NAME,"button")
            p_tags=[]
            for b in button_classes:
                try:
                    p_element = b.find_element(By.TAG_NAME, 'p')
                    p_tags.append(p_element)
                except Exception as q:
                     pass
            
            play_element=None
            
            for tag in p_tags:
                if tag.text=="Play":
                    play_element=tag
            return play_element
            
        except Exception as e:
            print(e)
    
    def get_tracks(self):
        play_element=self.open_tracks()  
        play_element.click()
        
    
            
        menu_class=self.driver.find_element(By.CLASS_NAME,"menu")
        track_container=menu_class.find_element(By.CLASS_NAME,"tracks-container")
        tracks=track_container.find_elements(By.CLASS_NAME,"track")

        track_buttons=[]
        for track in tracks:
            track_button=track.find_element(By.CLASS_NAME,"button")
            track_buttons.append(track_button)
        
        return track_buttons
    
    def open_track(self,track_number):
        try:
            track_buttons=self.get_tracks()
            ##test we need to prompt someway for track numer
            track_one=track_buttons[track_number-1]
            track_one.click()
            
            menu_class=self.driver.find_element(By.CLASS_NAME,"menu")
            
            track_info=menu_class.find_element(By.CLASS_NAME,"track-info")
            
            side_panel=track_info.find_element(By.CLASS_NAME,"side-panel")
           
            play_button=side_panel.find_element(By.TAG_NAME,"button")
            
            return play_button
        except IndexError as e:
            print("enter in a valid track number")
    
    def play(self):
        play_button=self.open_track(1)
        
        play_button.click()
        
        time.sleep(0.5)
        self.keyboard.press(Key.up)
        time.sleep(30)
    
        
        
        
        

driver=Driver()
driver.play()

