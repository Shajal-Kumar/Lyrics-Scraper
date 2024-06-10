from bs4 import BeautifulSoup as bs
import requests as req
from colorama import Fore
import time

singer_name = input(Fore.LIGHTYELLOW_EX + "Enter Singer Name:").capitalize().replace(' ', '-')
song_name = input(Fore.LIGHTRED_EX + "Enter Song Name:").lower().replace(' ', '-')

def get_lyrics(singer, song):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    html = req.get(f'https://genius.com/{singer}-{song}-lyrics', headers = header)
    soup = bs(html.text, 'lxml')
    grid = soup.find("div", class_="PageGriddesktop-a6v82w-0 SongPageGriddesktop-sc-1px5b71-0 Lyrics__Root-sc-1ynbvzw-0 iEyyHq")
    lyrics = grid.find_all("div", class_="Lyrics__Container-sc-1ynbvzw-1 kUgSbL")
    for verses in lyrics:
        verse = verses.find_all("span", class_="ReferentFragmentdesktop__Highlight-sc-110r0d9-1 jAzSMw")
        for line in verse:
            print(Fore.GREEN + line.text + '\n')
    print(Fore.LIGHTWHITE_EX + '------------END------------')

if __name__ == '__main__':
    try:
        print(Fore.CYAN + f"-----GETTING LYRICS FOR {song_name.upper()} by {singer_name.capitalize()}-----")
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        print()
        get_lyrics(singer_name, song_name)
        
    except:
        print(Fore.RED + "SONG NOT FOUND!!")