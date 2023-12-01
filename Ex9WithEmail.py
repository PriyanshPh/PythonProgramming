# Akhbaar padhke sunaao
import requests
import json
def Any(str):
    from win32com.client import Dispatch
    Spk = Dispatch("SAPI.SpVoice")
    Spk.Speak(str)
if __name__ == '__main__':
    Any("Today news are start now")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=75afc54ff56d4c49ac9149ca12c2bfc1"
    news = requests.get(url).text
    PH = json.loads(news) # loads is used to read strings
    print(PH["articles"])
    arts = PH['articles']
    for article in arts:
        print(article['title'])
        Any(article['title'])
        Any("Moving on to the next news now")
    Any("Now today news end")
# harisalikhan13@gmail.com