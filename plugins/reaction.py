from pyrogram import Client, filters
from pyrogram.types import Message
from ChampuMusic import app
# Define the command and emoji for the reaction
@app.on_message(filters.command("react"))
async def react_to_message(client, message: Message):
    # Check if the command is a reply to another message
    if message.reply_to_message:
        try:
            # Get the emoji from the command argument, default to '👍' if not provided
            emoji = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else '👍'
            
            # Send the reaction to the replied message
            await client.send_reaction(
                chat_id=message.chat.id,
                message_id=message.reply_to_message.id,
                emoji=emoji
            )
            await message.reply(f"Reaction {emoji} sent successfully!")
        except Exception as e:
            await message.reply(f"Failed to send reaction. Error: {str(e)}")
    else:
        await message.reply("Please reply to a message to react to it.")

# New function to automatically react to new posts in a channel
@app.on_message(filters.channel)
async def auto_react_to_channel_post(client, message: Message):
    try:
        # Send a reaction to the new message
        await client.send_reaction(
            chat_id=message.chat.id,
            message_id=message.id,
            emoji='👍'  # You can change this to any emoji you prefer
        )
        print(f"Reacted to message {message.id} in channel {message.chat.title}")
    except Exception as e:
        print(f"Failed to react to channel post. Error: {str(e)}")