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
		username = message.content[len(command):]
		
		# Want to have just the name without discrim for later
		nickname = username
		print("username: " + nickname)
		
		# Get all members of the server to search for the right user. 
		#members = client.get_all_members()
		members = message.server.members
		
		
		# TODO: Check if there is more than 1 user with the given name.
		# Should be working.
		userCount = 0
		for x in members:
			print(x)
			if x.name == username:
				userCount += 1
				print(userCount)
		
		if userCount >= 2:
			await client.send_message(message.channel, "Uh-oh! There are multiple users with that username on the server! Who is the right person?")
			await client.send_message(message.channel, "Please type a period followed by the 4 digit number at the end of their username.")
			msg = await client.wait_for_message(author = message.author)
			discrim = msg.content
			discrim = discrim[1:]
#			print(discrim)
			username = username + str('#') + discrim
			userWithDiscriminator = message.server.get_member_named(username)
#			print("user is " + username)
			
		else:
			userWithDiscriminator = discord.utils.get(members, name = message.content[len(command):])
		
		print(userWithDiscriminator)
		
		if username == "poke-bot":
			await client.send_message(message.channel, "You can't poke yourself!")
		
		# Send a private message to the correct user.
		elif userWithDiscriminator is not None:
			await client.send_message(userWithDiscriminator, 'Hey {}! {} is online and wants to join up!'.format(nickname, message.author.name))
	
		# Handle the case of no user with the inputted name being on the server.
		elif userWithDiscriminator is None or username == "poke-bot":
			await client.send_message(message.channel, 'No user with that username found on this server!')
	
		# Print members for debugging purposes.
		#for x in members:
		#	print(x)
		
		#TODO: Add message saying the PM has been sent.
		
client.run(config.token)
