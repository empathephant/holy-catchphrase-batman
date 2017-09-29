import re
import os
import random
import download_episodes

if not os.path.isdir("episodes"):
    download_episodes.scrape_all_seasons()

if not os.path.isfile("catchphrases.txt"):
    catchphrases = open("catchphrases.txt", "a+")

    screenplay_re = r'(?<=<div class="scrolling-script-container">)(.*?)(?=</div>)'
    holy_re = r'holy[^.,?!]*'

    for filename in os.listdir('episodes'):
        current_episode = open(os.path.join('./episodes', filename),"r")
        episode_text = current_episode.read()
        screenplay_text = re.search(screenplay_re, episode_text, re.DOTALL)

        for match in re.findall(holy_re, screenplay_text.group(0), re.IGNORECASE):
            catchphrases.write(match + ", Batman!\n")
        current_episode.close()
    catchphrases.close()

catchphrases = open("catchphrases.txt")
phrases = catchphrases.readlines()
phrases = [x.strip() for x in phrases]

character_entered = input("Type any key to generate an exclamation of surprise, or type \'q\' to quit: ")
while character_entered != 'q':
    print(random.choice(phrases) + "\n")
    character_entered = input("Type any key to get another expression, or type \'q\' to quit: ")
print("Holy exit, Batman! Goodbye!")
