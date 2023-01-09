import random

def respond(message):
  # Check for a greeting
  if message in ["hi", "hello", "greetings", "hey"]:
    return "Hello!"
  # Check for a farewell
  if message in ["goodbye", "farewell", "bye"]:
    return "Goodbye!"
  # Respond with a random message
  responses = ["I see.", "Interesting.", "I'm not sure I understand.", "Can you elaborate?", "Go on."]
  return random.choice(responses)

# Start a conversation
print("Hello! How are you today?")
while True:
  message = input(">> ")
  print(respond(message))
  # End the conversation if the user says goodbye
  if message in ["goodbye", "farewell", "bye"]:
    break
