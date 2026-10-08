import random

from openai import OpenAI
# CONFIGURATION
model="nvidia/nemotron-3-nano-4b" # used embedding model to understand reasoning etc plus 4 gb so wont eat up too much memory
maximumiter=3
subject="Oblique Block Lanczos"
seed="IDK anything in Lanczos teach me oblique block lanczos and then other things like how to use it in practice and what are the advantages and disadvantages of it"
# open ai sdk
client=OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
    )
bots=["Alice","Bob"]
using_bot=random.choice(bots)
convo=seed
print("Model:"+model)
print("Subject:"+subject)
print("Total Rounds:",maximumiter)
for i in range(maximumiter):
    print("Round:",i+1)
    print("Using Bot:",using_bot)
    response=client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": convo}
    ],
    max_tokens=3000
    )
    answer=response.choices[0].message.content
    print(using_bot,":",repr(answer))
    convo = convo + f"\n\n{using_bot}: {answer}"

    if using_bot=="Alice":
        using_bot="Bob" 
    else:
        using_bot="Alice"

print("!!! Finished !!!")