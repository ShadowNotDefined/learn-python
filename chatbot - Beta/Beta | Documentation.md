# AIML Chatbot Documentation

This documentation outlines the steps to set up a basic chatbot using the `aiml` (Artificial Intelligence Markup Language) library in Python. This bot leverages AIML files for chatbot responses and maintains its conversational state with a saved brain dump.

## Prerequisites

Ensure you have the `aiml` library installed. This library handles AIML-based chatbots in Python.

```bash
pip install aiml
```

## Code Overview

Below is a breakdown of the chatbot setup and interaction code.

### 1. Import the AIML Library

The code begins by importing the `aiml` library, which is used for creating and interacting with the AIML Kernel.

```python
import aiml
```

### 2. Create the Kernel Object

The Kernel object is the core of the AIML chatbot, which processes the user input and provides responses.

```python
# Create the Kernel object
kernel = aiml.Kernel()
```

### 3. Load AIML Files

AIML files contain the rules and responses for the chatbot. In this example, the `startup.aiml` file is loaded first, which usually includes instructions to load other AIML files.

```python
# Load the AIML files
kernel.learn("startup.aiml")
kernel.respond("load aiml b")
```

### 4. Define a Function for Chatbot Responses

The `chatbot_response` function takes user input and returns a response from the chatbot. It also saves the current state of the chatbot to a file called `brain.dump`, enabling the bot to remember its state between sessions.

```python
def chatbot_response(user_input):
    # Get the bot's response to the user input
    bot_output = kernel.respond(user_input)
    
    # Save the bot's current state
    kernel.saveBrain("brain.dump")
    
    # Return the bot's response
    return bot_output
```

### 5. Run an Interactive Chat Loop

The code runs an infinite loop to continually get user input, pass it to the chatbot, and print the bot's response. To exit the loop, use `Ctrl + C` or close the terminal.

```python
# Get user input and generate bot output
while True:
    user_input = input("User: ")
    bot_output = chatbot_response(user_input)
    print("Beta: " + bot_output)
```

### Full Example Code

Below is the complete code example for setting up and running the chatbot:

```python
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
    user_input = input("User: ")
    bot_output = chatbot_response(user_input)
    print("Beta: " + bot_output)
```

### Notes

- **AIML Files:** Ensure `startup.aiml` and any referenced AIML files are available in the same directory or provide the correct file path.
- **State Saving:** The brain dump (`brain.dump`) allows the bot to maintain state across sessions, saving memory and improving continuity.
- **Exiting the Chat Loop:** Use `Ctrl + C` to stop the loop if needed.

### Conclusion

This code provides a basic AIML chatbot framework. Customize your AIML files to adjust the bot's responses and enhance conversational depth. This setup saves the bot's state, allowing for more natural, continuous interactions over time.