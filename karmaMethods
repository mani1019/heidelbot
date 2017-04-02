import operator,pickle
users = {"Franky":0, "@TheGlitchHam":0,"@dawu1986":0,"@Jominator":0,"@Atera97":0,"@Schlaumayer":0,"@TerenceChill":0,"@DonDyaego":0,"Buffy":0}

def register(bot, update,args):
    if args[0] in users:
      bot.sendMessage(chat_id=update.message.chat_id, text="User is already registered")
    else:
        users[args[0]]=0
        bot.sendMessage(chat_id=update.message.chat_id, text=args[0]+" is now registered")

def getUsers(bot, update):
    message="Registered users are:\n"
    for name in users:
        message=message+name+" "
    bot.sendMessage(chat_id=update.message.chat_id, text=message)

def top(bot, update):
    message="Top 10 users are:\n"
    sorted_x = sorted(users.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(10):
        if i<len(sorted_x):
            message=message+str(sorted_x[i])+"\n"
    bot.sendMessage(chat_id=update.message.chat_id, text=message)
    
def plus(bot, update, args):
    if args[0] in users:
       karma=users[args[0]]
       karma=karma+1
       users[args[0]]=karma
       try:
        bot.sendMessage(chat_id=update.message.chat_id, text="Karma of '"+args[0]+"' is now "+str(karma))
       except TelegramError:
        bot.sendMessage(chat_id=update.message.chat_id, text="KKarma of '"+args[0]+"' is now "+str(karma))
    else:
       bot.sendMessage(chat_id=update.message.chat_id, text=args[0]+" is no registered user. Please use /register")
       

def minus(bot, update, args):
    if args[0] in users:
       karma=users[args[0]]
       if karma > 0:
           karma=karma-1
       users[args[0]]=karma
       bot.sendMessage(chat_id=update.message.chat_id, text="Karma of '"+args[0]+"' is now "+str(karma))
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text=args[0]+" is no registered user. Please use /register")
       
def dumpKarma(bot, update):
    with open('karmafile.pickle', 'wb') as fp:
        pickle.dump(users, fp)
        bot.sendMessage(chat_id=update.message.chat_id, text='Karma in Datei abgelegt.')

def loadKarma(bot, update):
    with open ('karmafile.pickle', 'rb') as fp:
        karmaList = pickle.load(fp)
    users.update(karmaList)
    bot.sendMessage(chat_id=update.message.chat_id, text='Karma aus Datei gelesen.')
