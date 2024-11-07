import aiml
	
# Create the Kernel object
kernel = aiml.Kernel()

# Load the AIML files
kernel.learn("startup.aiml")
kernel.respond("load aiml b")

# Define a function to handle user input and generate bot output
def chatbot_response(user_input):
    # Get the bot's response to the user input
    bot_output = kernel.respond(user_input)
    
    # Save the bot's current state
    kernel.saveBrain("brain.dump")
    
    # Return the bot's response
    return bot_output

# Get user input and generate bot output
while True:
    user_input = raw_input("User: ")
    bot_output = chatbot_response(user_input)
    print("Beta: " + bot_output)

