import setcreds
import openai

# completion = openai.Completion.create(
#     engine="davinci", 
#     max_tokens=32, 
#     temperature=0.2,
#     prompt="""Roses are red, 
# violets are blue,
# """
# )

# for ix, choice in enumerate(completion.choices):
#     print(f"choice {ix}: {choice.text}")

print("Try talking to the AI")
user_msg = input(">>> ")
user_messages = []
ai_messages = []

while user_msg != "exit":
    user_messages += [user_msg]

    prompt = """A user and an AI are talking. The user is asking the ai questions about itself. The ai
is responding with interesting observations, about the weather, about the user's favorite color,
and about sheep. The ai likes to talk about sheep and Bach.
""" + "\n".join([
        val for pair in zip(
            [f"user says: {msg}" for msg in user_messages], 
            [f"ai says: {msg}" for msg in ai_messages + [""]], 
        )
        for val in pair
    ])

    # print (f"=================")
    # print (f"{prompt}")
    # print (f"=================")

    got_ai_msg = False
    temperature = 0
    tries_remaining = 10
    while tries_remaining and not got_ai_msg:
        tries_remaining -= 1
        
        temperature = min(2, temperature + 0.1)

        completion = openai.Completion.create(
            engine="davinci", 
            max_tokens=32, 
            temperature=temperature,
            prompt=prompt,
            frequency_penalty=1.0
        )

        ai_raw_msg = completion.choices[0].text

        ai_msg_lines = ai_raw_msg.split("\n")

        ai_msg = ai_msg_lines[0]

        got_ai_msg = not ai_msg in ai_messages

    ai_messages += [ai_msg]

    print(f"OpenAI says: {ai_msg}")

    user_msg = input(">>> ")
