from src.chat import Chat

chat_obj = Chat(message="hello", context="you are a helpful assistant", candidates=4, temperature=1)

for i in range(3):
    message = input("enter message : ")
    answer = chat_obj.reply(message=message)
    print(answer)
print(chat_obj.get_chat_history())
