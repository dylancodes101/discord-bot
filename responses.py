import random
import search
import sci


def get_response(message: str) -> str:


    if "!youtube:" in message:
        yt = message.replace("!youtube:",'')
        yt = yt.strip()
        subs = search.get_youtube_subscriber_count(yt)
        subs = str(sci.format_e(subs))
        return subs
        print(yt)
        print(subs)
    p_message = message.lower()

    

    if p_message == '!hello':
        return 'Hey there!'

    if message == '!roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`This is a help message that you can modify.`'
    


    #return 'I didn\'t understand what you wrote. Try typing "!help".'