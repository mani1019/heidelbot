import pickle
newsList=[]

def getNews(bot, update):
    getnews='Die aktuellen News der Heidelbohnen sind:\n'
    for num,news in enumerate(newsList, start=1):
        getnews=getnews+str(num)+": "+news+'\n'
    bot.sendMessage(chat_id=update.message.chat_id, text=getnews)
    

def addNews(bot, update, args):
    if not args:
        bot.sendMessage(chat_id=update.message.chat_id, text='Leere News sind nicht erlaubt.') 
    else:
        string=''
        for arg in args:
            string=string+' '+arg    
        newsList.append(string)
        bot.sendMessage(chat_id=update.message.chat_id, text='News hinzugefuegt.')
    
def removeNews(bot, update, args):
    try:
        args.sort(key=int, reverse=True)
        for num in range(len(args)):        
            newsList.pop(int(args[num])-1)
        bot.sendMessage(chat_id=update.message.chat_id, text='News geloescht.')
    except ValueError:
        bot.sendMessage(chat_id=update.message.chat_id, text='Keine Zahl.')
    except IndexError:
        bot.sendMessage(chat_id=update.message.chat_id, text='Ungueltige Zahl.')

def removeAllNews(bot, update):
    del newsList[:]
    bot.sendMessage(chat_id=update.message.chat_id, text='Alle News geloescht.')

def dumpNews(bot, update):
    with open('newsfile.pickle', 'wb') as fp:
        pickle.dump(newsList, fp)
        bot.sendMessage(chat_id=update.message.chat_id, text='News in Datei abgelegt.')

def loadNews(bot, update):
    with open ('newsfile.pickle', 'rb') as fp:
        news3List = pickle.load(fp)
    newsList.extend(news3List)
    getnews='Die geladenen News der Heidelbohnen sind:\n'
    for num,news in enumerate(news3List, start=1):
        getnews=getnews+str(num)+": "+news+'\n'
    bot.sendMessage(chat_id=update.message.chat_id, text=getnews)
