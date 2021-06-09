messages = ['hello', '你好', 'hi', "what's up"]
sent_messages = []


def show_messages(messages, sent_messages):
    while messages:
        sent_message = messages.pop()
        sent_messages.append(sent_message)
        print(sent_message)


show_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)
