import requests as r
import os

headers = {'user-agent': 'Shanti der Blatter (empathephant@gmail.com)'}

def scrape_season(episode, season):
    if episode < 10:
        episode_url = "https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=batman-1966&episode=s0" + season + "e0" + str(episode_num)
    else:
        episode_url = "https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=batman-1966&episode=s0" + season + "e" ++ str(episode_num)
    episode_text = r.get(episode_url, headers=headers)
    filename = "s" + season + 'e' + str(episode) + ".txt"
    f = open(os.past.join(episodes, filename),"w+")
    f.write(episode_text.text)
    f.close

def scrape_all_seasons():
    os.makedirs("episodes")

    #season 1
    for episode_num in range(1, 35):
        scrape_season(episode_num, '1')
        time.sleep(random.uniform(1.5, 2.5))

    #season 2
    for episode_num in range(1, 61):
        scrape_season(episode_num, '2')
        time.sleep(random.uniform(1.5, 2.5))

    #season 3
    for episode_num in range(1, 27):
        scrape_season(episode_num, '3')
        time.sleep(random.uniform(1.5, 2.5))
