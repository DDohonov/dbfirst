
import telebot
import os
import sqlite3

PATH = os.path.abspath(__file__ + "/..")

connect = sqlite3.connect(os.path.join(PATH, "mydb.db"), check_same_thread=False)

cursor = connect.cursor()

check_id = '''
SELECT chat_id FROM users'''


bot = telebot.TeleBot('5970658595:AAHgZ_aUyFw-urXX2IZWx3pRfadQ6DNjS7M')                      

@bot.message_handler(commands=["start"])

def start(message):
    result = cursor.execute(check_id)
    flag = True
    # print(result.fetchall()) # получить все объекты 
    print(message.chat.id)
    for i in result.fetchall():
        if i[0] == message.chat.id:
            flag = False
            break
    if flag == True:
        msg = bot.send_message(message.chat.id,"Здравствуйте, как вы хотите, чтоб я вас называл?")
        bot.register_next_step_handler(msg, get_nickname)
    else: 
        bot.send_message(message.chat.id,"Ky")
def get_nickname(message):
    add_user = f'''
    INSERT INTO users
    VALUES ('{message.chat.id}','{message.from_user.first_name}','{message.from_user.last_name}','{message.from_user.username}', '{message.text}')
    '''
    cursor.execute(add_user)
    connect.commit()
    bot.send_message(message.chat.id,"Все готово")
bot.infinity_polling()









# chat_id firstname lastname username nickname 

# sql1 = '''
# CREATE TABLE users (
#     chat_id int,
#     firstname varchar(255),
#     lastname varchar(255),
#     username varchar(255),
#     nickname varchar(255)
# );
# # '''
# add_user = '''
#     INSERT INTO users
#     VALUES ('542387853','Dima','Dima','Dima', 'Dima')
# '''
# cursor.execute(add_user)
# connect.commit()