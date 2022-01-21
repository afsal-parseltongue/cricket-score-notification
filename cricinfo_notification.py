
import requests
from bs4 import BeautifulSoup
import os
import time




def get_score_and_notify():
    url = "https://www.espncricinfo.com/series/india-in-south-africa-2021-22-1277060/south-africa-vs-india-2nd-odi-1277083/live-cricket-score"
    response  = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    score_parent = soup.find('div', attrs = {'class':'match-info match-info-MATCH match-info-MATCH-full-width'})

    batting_team_div = score_parent.find("div", attrs={"class": "team"})
    name_div = batting_team_div.find('p', attrs = {'class': 'name'})
    overs_div = batting_team_div.find('span', attrs={"class": 'score-info'})
    score_div = batting_team_div.find_all('span', attrs={"class": "score"})


    batting_team_name = name_div.text
    display_text = ""
    if batting_team_name:
        display_text += batting_team_name
        display_text += " "
    overs_text = overs_div.text
    if overs_text:
        display_text += overs_text
        display_text += " "

    scores = []
    for span in score_div:
        scores.append(span.text.replace("\xa0", " "))



    scores_string = "".join(scores)

    if scores_string:
        display_text += scores_string


    cmd = f'/usr/bin/notify-send "Cricket Score" "{display_text}"'
    os.system(cmd)


starttime = time.time()
while True:
    print("tick")
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
    get_score_and_notify()


