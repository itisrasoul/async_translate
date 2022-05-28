from async_get import main
from bs4 import BeautifulSoup
import sys
from config import SRC_LANG, DEST_LANG

def add_trs(text_list: list) -> str:
    trs_urls = []
    for text in text_list:
        trs_urls.append(dict(origin_text=text, translate_url=f"https://translate.google.com/m?tl={DEST_LANG}&sl={SRC_LANG}&q="+text.strip()))
    return trs_urls

def translate(text_list):
    translated_texts = main([each['translate_url'] for each in text_list], 5, mode='text')
    for each in translated_texts:
        for text in text_list:
            if text['translate_url'] == each['url']:
                print(text['origin_text']+": "+BeautifulSoup(each['response'], "html5lib").find("div", {"class": "result-container"}).contents[0])

if __name__ == "__main__":
    print("Total words: ", len(sys.argv[1:]))
    url_list = add_trs(sys.argv[1:])
    translate(url_list)