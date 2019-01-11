from bs4 import BeautifulSoup as bs
import re,csv, os
import pandas as pd
from tqdm import tqdm

FolderHtml = './Indosat/'

def crawlFiles(dPath,types=None): # dPath ='C:/Temp/', types = 'pdf'
    if types:
        return [dPath+f for f in os.listdir(dPath) if f.endswith('.'+types)]
    else:
        return [dPath+f for f in os.listdir(dPath)]

List_files = crawlFiles(FolderHtml,types='htm')
Save_Path = './Indosat.csv'

def htmcsv(files,fName):
    if __name__ == "__main__":

        urlPattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        print('Loading Data: ', flush = True)
        Tweets, Username, waktu, replies, retweets, likes, Language =  [], [], [], [], [], [], []
        urlStatus, D = [], []
        # fData = allData[0]
        for fData in tqdm(files):
            soup = bs(open(fData,encoding='utf-8', errors = 'ignore', mode='r'),'html.parser')
            data = soup.find_all('li', class_= 'stream-item')
            # t = data[0]
            for i,t in tqdm (enumerate(data)):
                    # Loading tweet
                    T = t.find_all('p',class_='TweetTextSize')[0]
                    T = bs(str(T),'html.parser').text
                    Tweets.append(T)
                    # Loading UserName
                    U = t.find_all('span',class_='username')
                    U = bs(str(U[0]),'html.parser').text
                    Username.append(U)
                    # Loading Time
                    T = t.find_all('a',class_='tweet-timestamp')[0]
                    T = bs(str(T),'html.parser').text
                    waktu.append(T)
                    # Loading reply, retweet & Likes
                    RP = t.find_all('span',class_='ProfileTweet-actionCountForAria')[0]
                    RT = t.find_all('span',class_='ProfileTweet-actionCountForAria')[1]
                    L  = t.find_all('span',class_='ProfileTweet-actionCountForAria')[2]
                    RP = int((bs(str(RP), "lxml").text.split()[0]).replace('.','').replace(',',''))
                    RT = int((bs(str(RT), "lxml").text.split()[0]).replace('.','').replace(',',''))
                    L = int((bs(str(L), "lxml").text.split()[0]).replace('.','').replace(',',''))
                    replies.append(RP)
                    retweets.append(RT)
                    likes.append(L)
                    # Loading Bahasa
                    try:
                        L = t.find_all('span',class_='tweet-language')
                        L = bs(str(L[0]), "lxml").text
                    except:
                        L =''
                    Language.append(L)

                    url = str(t.find_all('small',class_='time')[0])
                    try:
                        url = re.findall(urlPattern,url)[0]
                    except:
                        try:
                            mulai, akhir = url.find('href="/')+len('href="/'), url.find('" title=')
                            url = 'https://twitter.com/' + url[mulai:akhir]
                        except:
                            url = ''
                    urlStatus.append(url)

        print('Saving Data to "%s" ' %fName, flush = True)
        dfile = open(fName, 'w', encoding='utf-8', newline='')
        dfile.write('Time, Username, Tweet, Replies, Retweets, Likes, Language, urlStatus\n')
        with dfile:
            writer = csv.writer(dfile)
            for i,t in enumerate(Tweets):
                writer.writerow([waktu[i],Username[i],t,replies[i],retweets[i],likes[i],Language[i],urlStatus[i]])
        dfile.close()
        print('All Finished', flush = True)

htmcsv(List_files,Save_Path)