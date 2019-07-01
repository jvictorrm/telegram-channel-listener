from telethon import functions, types
from telethon.sync import TelegramClient
import asyncio
import time
import configparser


""" init config """
config = configparser.ConfigParser()
config_file_name = 'config.ini'
if not config.read(config_file_name):
	print('Erro no arquivo de configuração: Arquivo não encontrado!')
	exit()

session_name = 'client'
api_id = config['telegram_auth']['api_id']
api_hash = config['telegram_auth']['api_hash']
channel = config['telegram_target']['channel']

""" start telegram client listener """
with TelegramClient(session_name, api_id, api_hash) as client:
    while client.is_connected:
        dialogs = client.get_dialogs()
        dialog = None
        for d in dialogs:
            if d.entity.username == channel:
                dialog = d
                break
        
        if not dialog:
            print('Nenhum canal com o nome de usuário "{channel}" foi encontrado.'.format(channel=channel))
            exit()
        
        if dialog.unread_count > 0:
            chats = client.get_messages(channel, dialog.unread_count)

            for chat in chats:
                # record data
                thumb_filename = 'thumb.jpg'
                title_media_message = chat.media.webpage.title
                url_media_message = chat.media.webpage.url
                chat.download_media(thumb_filename)

            entity_channel = client.get_entity(channel)
            # result = client.send_read_acknowledge(entity_channel)  # mark channel as read
            print(dialog.id, dialog.title, dialog.unread_count, dialog.archived, dialog.entity.username, entity_channel)        
        time.sleep(60 * 10) # wait 10 minutes
    client.run_until_disconnected()