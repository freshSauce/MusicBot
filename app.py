from pytgcalls import PyTgCalls, idle
from pytgcalls.types import MediaStream, AudioParameters, AudioQuality
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from dotenv import load_dotenv
import yt_dlp


from utils import prefixes, welcome_message
from custom_filters import has_args
from modules import youtubeSearch

import os

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
playing = False
queue = []

if "FreshMusic.session" not in os.listdir(
    os.path.dirname(os.path.abspath(__file__))
):  # noqa
    app = Client("FreshMusic", api_id=api_id, api_hash=api_hash)  # noqa
else:
    app = Client("FreshMusic")

player = PyTgCalls(app)


def get_youtube_stream(link) -> (str, str):
    with yt_dlp.YoutubeDL(
        {
            "format": "bestaudio",
            "forceurl": True,
            "quiet": True,
            "simulate": True,
        }  # noqa
    ) as extractor:  # noqa
        data = extractor.extract_info(link)
        return data["url"]


@player.on_stream_end()
async def next_song(client, message):
    global queue
    try:
        next_song = queue.pop(0)
    except Exception:
        pass
    else:
        print("SONG ENDED")

        remote = get_youtube_stream(next_song["url"])
        await app.send_message(
            chat_id=message.chat_id,
            text=f"Reproduciendo __{next_song['title']}__ de **{next_song['author']}**",  # noqa
        )
        await player.change_stream(
            message.chat_id,
            MediaStream(
                media_path=remote,
                audio_parameters=AudioParameters.from_quality(
                    AudioQuality.HIGH
                ),  # noqa
                video_flags=MediaStream.IGNORE,
            ),
        )


@app.on_message(filters.command("skip", prefixes=prefixes))
def skip_song(client, message):
    global queue
    try:
        next_song = queue.pop(0)
    except IndexError:
        client.send_message(
            chat_id=message.chat.id,
            text=f"¡No hay canciones en cola!",  # noqa
            reply_to_message_id=message.id,  # noqa
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text=f"Reproduciendo __{next_song['title']}__ de **{next_song['author']}**",  # noqa
            reply_to_message_id=message.id,  # noqa
        )
        remote = get_youtube_stream(next_song["url"])
        player.change_stream(
            message.chat.id,
            MediaStream(
                media_path=remote,
                audio_parameters=AudioParameters.from_quality(
                    AudioQuality.HIGH
                ),  # noqa
                video_flags=MediaStream.IGNORE,
            ),
        )


@app.on_message(filters.command("start", prefixes=prefixes))
def start(client, message):
    client.send_message(
        chat_id=message.chat.id,
        text=welcome_message,
        reply_to_message_id=message.id,  # noqa
    )


@app.on_message(filters.command("play", prefixes=prefixes) & has_args)
def play(client, message):
    global playing
    video = youtubeSearch(" ".join(message.command[1:]))

    if video[0] and not playing:
        remote = get_youtube_stream(video[1]["url"])
        client.send_message(
            chat_id=message.chat.id,
            text=f"Reproduciendo __{video[1]['title']}__ de **{video[1]['author']}**",  # noqa
            reply_to_message_id=message.id,  # noqa
        )
    elif video[0] and playing:
        client.send_message(
            chat_id=message.chat.id,
            text=f"Añadiendo __{video[1]['title']}__ de **{video[1]['author']}** a la cola",  # noqa
            reply_to_message_id=message.id,  # noqa
        )
        queue.append(video[1])
        return
    else:
        client.send_message(
            chat_id=message.chat.id,
            text=video[1],  # noqa
            reply_to_message_id=message.id,  # noqa
        )
        return

    try:
        player.join_group_call(
            message.chat.id,
            MediaStream(
                media_path=remote,
                audio_parameters=AudioParameters.from_quality(
                    AudioQuality.HIGH
                ),  # noqa
                video_flags=MediaStream.IGNORE,
            ),
        )
    except ChatAdminRequired:
        client.send_message(
            client.send_message(
                chat_id=message.chat.id,
                text="No fue posible iniciar la reproducción. El bot necesita permisos de administrador.",  # noqa
                reply_to_message_id=message.id,  # noqa
            )
        )
    else:
        playing = True


player.start()


idle()
