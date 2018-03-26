import discord
import asyncio
import config

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('-----')

# TODO: Handle getting the right user if there are 2
#		or more users with the same username.
	
@client.event
async def on_message(message):
	# Command that begins the process of sending a private message.
	if message.content.startswith('!poke'):
		command = '!poke '
		#author = message.author.name
		#print(author)
		
		# Use the length of command string in case the command changes.
		print(message.content[len(command):])
		username = message.content[len(command):]
		print("username: " + username)
		
		# Get all members of the server to search for the right user. 
		members = client.get_all_members()
		userWithDiscriminator = discord.utils.get(members, name = message.content[len(command):])
		
		#TODO: Check if there is more than 1 user with the given name.
		
		print(userWithDiscriminator)
		
		if username == "poke-bot":
			await client.send_message(message.channel, "You can't poke yourself!")
		
		# Send a private message to the correct user.
		elif userWithDiscriminator is not None:
			await client.send_message(userWithDiscriminator, 'Hi {}! {} is online'.format(username, message.author.name))
	
		# Handle the case of no user with the inputted name being on the server.
		elif userWithDiscriminator is None or username == "poke-bot":
			await client.send_message(message.channel, 'No user with that username found on this server!')
	
		# Print members for debugging purposes.
		for x in members:
			print(x)
		
client.run(config.token)
