print("hello world")
# the run command for python files is python3 "the file name".py 
# welcome back to earth lol 
# ---------------------------------------------------------------------------------
# need to add more explanation for the below steps. Just super tired today.





from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
generator.model.config.pad_token_id = generator.model.config.eos_token_id
# weird error solved where it kepted out putting this: Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.

# prompt = "The New York Jets"
prompt = "software engineering"

result = generator(prompt, max_length=25, do_sample=True, temperature=0.9)



# print(result)
# returns a list with the only item in the list being a dictionary. 


# print(result[0]['generated_text'])
# we want the 0th item in the the list. Then we want to get the item in the dict with the key called "generated text"


print(result[0]['generated_text'].upper())
# because we are asking for a string back we can use string manipulation in python to show that it works

# feeling good about the result of the ai part sooooooooo now api stuff 

# --------------------------------------------------------------------------------------------------------------------------------------

# api's in python: https://www.youtube.com/watch?v=hpc5jyVpUpw

# just a youtube search for linkedin api: https://www.youtube.com/results?search_query=linkedin+api+