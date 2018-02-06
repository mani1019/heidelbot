from telegram.ext import Updater,CommandHandler
import logging,karmamethods as k
import newsmethods as n
updater = Updater(token='361500602:AAEPtaMTw0xhcJFqVyFz6D33kmMI3Liba8s')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def help(bot, update):
    handlerGroups = dispatcher.handlers
    handlers=handlerGroups.get(0)
    string='Commands:'
    for handler in handlers:
        string=string+'\n/'+str(handler.command)
        if handler.pass_args:
            string=string+' args'
    string=string+'\n'+'code at https://github.com/Schlaumayer/heidelbot'
    string=string+'\n'+'discord invite https://discord.gg/fgzsFwf'
    bot.sendMessage(chat_id=update.message.chat_id, text=string)   
    
def dump(bot, update):
    n.dumpNews(bot, update)
    k.dumpKarma(bot, update)

def load(bot, update):
    n.loadNews(bot, update)
    k.loadKarma(bot, update)

def bamboozle(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Bamboozled!!!")
    
plus_handler = CommandHandler('+', k.plus,pass_args=True)
plus_handler2 = CommandHandler('plus', k.plus,pass_args=True)
dispatcher.add_handler(plus_handler)                       
dispatcher.add_handler(plus_handler2)

minus_handler = CommandHandler('-', k.minus,pass_args=True)
minus_handler2 = CommandHandler('minus', k.minus,pass_args=True)
dispatcher.add_handler(minus_handler)
dispatcher.add_handler(minus_handler2)

register_handler = CommandHandler('register', k.register,pass_args=True)
dispatcher.add_handler(register_handler)

unregister_handler = CommandHandler('unregister', k.unregister,pass_args=True)
dispatcher.add_handler(unregister_handler)

getUsers_handler = CommandHandler('getusers', k.getUsers)
dispatcher.add_handler(getUsers_handler)

top_handler = CommandHandler('top', k.top)
dispatcher.add_handler(top_handler)

getnews_handler = CommandHandler('getnews', n.getNews)
dispatcher.add_handler(getnews_handler)

addnews_handler = CommandHandler('addnews', n.addNews,pass_args=True)
dispatcher.add_handler(addnews_handler)

removenews_handler = CommandHandler('removenews', n.removeNews,pass_args=True)
dispatcher.add_handler(removenews_handler)

removeallnews_handler = CommandHandler('removeallnews', n.removeAllNews)
dispatcher.add_handler(removeallnews_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

bam_handler = CommandHandler('anspruchsvolle', bamboozle)
dispatcher.add_handler(bam_handler)

dump_handler = CommandHandler('dump', dump)
dispatcher.add_handler(dump_handler)

load_handler = CommandHandler('load', load)
dispatcher.add_handler(load_handler)

               
updater.start_polling()
