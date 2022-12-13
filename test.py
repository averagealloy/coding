print("hello world")
# the run command for python files is python3 "the file name".py 
# welcome back to earth lol 
# ---------------------------------------------------------------------------------
# need to add more explanation for the below steps. Just super tired today.

from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')

# prompt = "The New York Jets"
prompt = "software engineering"

result = generator(prompt, max_length=25, do_sample=True, temperature=0.9)

print(result[0]['generated_text'])
# retuns the first item in result. with key "generated text" give us raw string


print(result[0]['generated_text'].upper())
# because we are asking for a string back we can use string manipulation