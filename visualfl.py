from openai import OpenAI
# connect to ai
client = OpenAI(api_key="")
# loop control
running = True
## creates the memory puts it in a list
memory = [
    {"role": "system", "content": "You are a helpful coding assistant."}
]
print("Ai assistant (type /exit to quit, /clear to reset, /history to view chat: ")
while running:
    user_input = input("You: ")
    ## exit condition obvs
    if user_input.lower() == "/exit":
        print("Goodbye!")
        running = False
    elif user_input.lower() == "/clear":
        ## This clears its memory somehow
        memory = [
            {"role": "system", "content": "You are a helpful coding assistant."}
        ]
        print("Memory Cleared")
        ##
    elif user_input.lower() == "/history":
        print("---- Converstation History ----")
        ## memory of all messages
        for msg in memory:
            ## this skips all the system role which are only for setting AI behavior
            if msg["role"] != "system":
                #msg['role'] gets "user" or assistant capitalize obviously makes the first letter uppercase
                #msg['content'] actually gets the content of the message
                #f"{formats it better }
                print(f"{msg['role'].capitalize()}: {msg['content']}")
        print("---------------------")
    else:
        try:
            # adds user messages to input memory
            memory.append({"role": "user", "content": user_input})
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=memory
            )
            #Gets Ai to reply
            ai_reply = response.choices[0].message.content

            #stores ai responses
            memory.append({"role": "assistant", "content": ai_reply})

            print("Ai:", ai_reply)
        except Exception as e:
            print("Error: ", e)