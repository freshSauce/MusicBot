from pyrogram import filters


async def has_args_filter(_, __, query):
    try:
        return len(query.text.split(" ")) > 1
    except AttributeError:
        return False


has_args = filters.create(has_args_filter)
