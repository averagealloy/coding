print("hello world")
# the run command for python files is python3 "the file name".py 
# welcome back to earth lol 
# ---------------------------------------------------------------------------------
# need to add more explanation for the below steps. Just super tired today.

from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')

# prompt = "The New York Jets"
prompt = "New York Yankees"

result = generator(prompt, max_length=25, do_sample=True, temperature=0.9)

print(result[0]['generated_text'])

