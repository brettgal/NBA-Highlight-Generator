from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
from moviepy.editor import VideoFileClip, concatenate_videoclips

options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option("prefs", {"download.default_directory" : "C:\\Users\\bgall\\Nba\\Videos"})

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.nba.com/game/den-vs-mia-0022200861/play-by-play?period=Q1")
driver.maximize_window()

acceptButton = driver.find_element(by=By.ID, value="onetrust-accept-btn-handler")
acceptButton.click()

closeButton = driver.find_element(by=By.CLASS_NAME, value="ab-close-button")
closeButton.click()

links = [x.get_attribute('href') for x in driver.find_elements(by=By.CLASS_NAME, value="StatEventLink_sel__pAwmA.GamePlayByPlayRow_statEvent__Ru8Pr")]
print(links)
i = 0
for link in links:
    if "Adebayo" in link:
        i = i + 1
        name = "Adebayo" + str(i) + ".mp4"
        driver.get(link)
        video = driver.find_element(by=By.CLASS_NAME, value="vjs-tech")
        video_url = video.get_property('src')
        urllib.request.urlretrieve(video_url, name)

driver.close()

j = 0
clipList = []
while j < i:
    clipList.append(VideoFileClip("Adebayo" + str(j + 1) + ".mp4"))
    j = j + 1

finalVid = concatenate_videoclips(clipList)

finalVid.write_videofile("finalVid.mp4")