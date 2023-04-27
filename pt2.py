import telebot
from jugaad_data.nse import NSELive
n = NSELive()

import requests
from telegram.ext import Updater, CommandHandler, MessageHandler
token="6159438806:AAGgzkFyNwsayDQUamOsWMdfLSYM8qPlQus"
bot = telebot.TeleBot(token)


@bot.message_handler(['start'])
def start(message) :
    bot.reply_to(message,"welcome to ticker bot \n /getLTP \n /all \n /toplooser \n /topgainers")   

@bot.message_handler(['getLTP']) 
def getLTP(message):
    bot.reply_to(message,"enter symbol \n /RELIANCE \n /TATAMOTORS \n /TATASTEEL \n /TCS \n /HDFCBANK \n /ICICIBANK \n /HINDUNILVR \n /ITC \n /INFY \n /HDFC \n /SBIN \n /BHARTIARTL \n /KOTAKBANK \n /BAJFINANCE \n /HCLTECH \n /ASIANPAINS \n /AXISBANK \n /MARUTI \n /TITAN \n /SUNPHARMA \n /ULTRACEMCO \n /ADANIENT \n /WIPRO \n /ONGC \n /JSWSTEEL \n /NTPC \n /POWERGRID \n /ADANIPORTS \n /COALINDIA \n /HDFCLIFE \n /GRASIM \n /SBILIFE \n /TECHM \n /HINDALCO \n /DIVISLAB \n /BPCL \n /CIPLA \n /TATACONSUM \n /APOLLOHOSP \n /UPL  ")
    bot.reply_to(message,message.text)

@bot.message_handler(['RELIANCE','TATAMOTORS','TATASTEEL','TCS','HDFCBANK','ICICIBANK','HINDUNILVR','ITC','INFY','HDFC','SBIN','BHARTIARTL','KOTAKBANK','BAJFINANCE','HCLTECH','ASIANPAINT','AXISBANK','MARUTI','TITAN','SUNPHARMA','ULTRACEMCO','ADANIENT','WIPRO','ONGC','JSWSTEEL','NTPC','POWERGRID','ADANIPORTS','COALINDIA','HDFCLIFE','GRASIM','SBILIFE','TECHM','HINDALCO','DIVISLAB','BPCL','CIPLA','TATACONSUM','APOLLOHOSP','UPL']) 
def cmp(message) :
    sym=message.text[1:]
    sym=sym.upper().strip()
    print(sym)
    q = n.stock_quote(str(sym))
       
    bot.reply_to(message,q['priceInfo']['lastPrice'])
   
    bot.reply_to(message,"/getLTP \n /all \n /toplooser \n /topgainers" )

@bot.message_handler(['all'])
def all(message) :
    for i in ['RELIANCE','TATAMOTORS','TATASTEEL','TCS','HDFCBANK','ICICIBANK','HINDUNILVR','ITC','INFY','HDFC','SBIN','BHARTIARTL','KOTAKBANK','BAJFINANCE','HCLTECH','ASIANPAINT','AXISBANK','MARUTI','TITAN','SUNPHARMA','ULTRACEMCO','ADANIENT','WIPRO','ONGC','JSWSTEEL','NTPC','POWERGRID','ADANIPORTS','COALINDIA','HDFCLIFE','GRASIM','SBILIFE','TECHM','HINDALCO','DIVISLAB','BPCL','CIPLA','TATACONSUM','APOLLOHOSP','UPL']:
        q = n.stock_quote(str(i))
        bot.reply_to(message,i+"="+str(q['priceInfo']['lastPrice']))
        
    bot.reply_to(message,"/getLTP \n /all \n /toplooser \n /topgainers" )


@bot.message_handler(['toplooser'])
def toplooser(message) :
    loose={}
    count=50
    for i in ['RELIANCE','TATAMOTORS','TATASTEEL','TCS','HDFCBANK','ICICIBANK','HINDUNILVR','ITC','INFY','HDFC','SBIN','BHARTIARTL','KOTAKBANK','BAJFINANCE','HCLTECH','ASIANPAINT','AXISBANK','MARUTI','TITAN','SUNPHARMA','ULTRACEMCO','ADANIENT','WIPRO','ONGC','JSWSTEEL','NTPC','POWERGRID','ADANIPORTS','COALINDIA','HDFCLIFE','GRASIM','SBILIFE','TECHM','HINDALCO','DIVISLAB','BPCL','CIPLA','TATACONSUM','APOLLOHOSP','UPL']:
        q = n.stock_quote(str(i))
        loose[i]=q['priceInfo']['pChange']
        
    
    loose = sorted(loose.items(), key=lambda x: x[1])
    
    bot.reply_to(message,"top loosers")
    count =0
    for key,value in loose :
        if count < 5 :
          bot.reply_to(message,key+"="+str(value))
          count=count+1
        else  :
            break
    


    bot.reply_to(message,"/getLTP \n /all \n /toplooser \n /topgainers" )

@bot.message_handler(['topgainers'])
def topgainers(message) :
    loose={}
    count=50
    for i in ['RELIANCE','TATAMOTORS','TATASTEEL','TCS','HDFCBANK','ICICIBANK','HINDUNILVR','ITC','INFY','HDFC','SBIN','BHARTIARTL','KOTAKBANK','BAJFINANCE','HCLTECH','ASIANPAINT','AXISBANK','MARUTI','TITAN','SUNPHARMA','ULTRACEMCO','ADANIENT','WIPRO','ONGC','JSWSTEEL','NTPC','POWERGRID','ADANIPORTS','COALINDIA','HDFCLIFE','GRASIM','SBILIFE','TECHM','HINDALCO','DIVISLAB','BPCL','CIPLA','TATACONSUM','APOLLOHOSP','UPL']:
        q = n.stock_quote(str(i))
        loose[i]=q['priceInfo']['pChange']
        
    
    loose =sorted(loose.items(), key=lambda item: item[1], reverse=True)
    
    bot.reply_to(message,"topgainers")
    count =0
    for key,value in loose :
        if count < 5 :
          bot.reply_to(message,key+"="+str(value))
          count=count+1
        else  :
            break
    


    bot.reply_to(message,"/getLTP \n /all \n /toplooser \n /topgainers " )

bot.polling()