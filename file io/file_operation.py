

file_path = 'sent_message.txt'
secret_message = 'Hey there! this is a secret message *wink*'
message_unsent = 'This message has been unsent'

with open(file_path, 'r+') as file:
    file.write(secret_message)

with open(file_path, 'r+') as file:
    origin_message = file.read()

    file.write(secret_message)
    file.seek(0)
    
    file.write(message_unsent)

    file.truncate(len(message_unsent))
    
print("Original mesasge: " + origin_message)
print("Message unsent: " + message_unsent)

    