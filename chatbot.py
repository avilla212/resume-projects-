import openai
import discord
import random

# Create a Discord client
client = discord.Client(intents=discord.Intents.all())

# Set your OpenAI API key
openai.api_key = "INSERT YOUR OPENAI API KEY HERE"

# Define a function to generate a response using GPT-3
async def generate_response(input_text):
    # Set the model engine to use
    model_engine = "text-davinci-002"
    
    # Set the prompt for the model
    prompt = (f"{input_text}\n")

    # Generate completions using the OpenAI API
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.7,
    )

    # Get the first completion as the response
    message = completions.choices[0].text
    return message

@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Get the input text
    if message.content.startswith('!'):
        input_text = message.content[1:]
        # Generate a response using GPT-3
        response = await generate_response(input_text)
    
        # Send the response to the text channel
        await message.channel.send(response)
        
        #if the user types !guess the game will start
        if message.content.startswith('!guess'):
            await guess_number()

#guess the number game
async def guess_number():
    numTries = 0 
    num = random.randint(1, 100)
    while True:
        #get the message from the user
        msg = await client.wait_for('message')
        #check if the message is a number
        if msg.content.isdigit():
            #convert the message to an int
            guess = int(msg.content)
            
            #check if the guess is correct
            if guess == num:
                await msg.channel.send('You got it!')
                break
            #check if the guess is too high
            elif guess > num:
                await msg.channel.send('Too high!')
                numTries += 1
                
            #check if the guess is too low
            elif guess < num:
                await msg.channel.send('Too low!')
                numTries += 1
    # print the number of tries it took to guess the number
    await msg.channel.send(f'You got it in {numTries} tries!')

@client.event
async def play_game(message):
    #when someone types !guess the game will start
    if message.content.startswith('!guess'):
        await guess_number()

@client.event
async def on_ready():
    print("Bot is ready.")

client.run("INSERT YOUR DISCORD BOT TOKEN HERE")
