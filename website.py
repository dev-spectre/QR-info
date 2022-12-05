import openai
import re

def deshuffle(shuffled_str):

    deshuffled_str = ""

    for i in range(0, len(shuffled_str)):
        ascii_val = ord(shuffled_str[i])
        ascii_val -= i
        deshuffled_str += chr(ascii_val)

    return deshuffled_str

openai.api_key = deshuffle("sl/[GU|y[Wdm[^xv\RzkK[}chrnWXxyx|]d§©f")
    

def get_info_from_ai(url):
    response = openai.Completion.create(
      model = "text-davinci-003",
      prompt = f"give me information about the website {url}",
      temperature = 0.7,
      max_tokens = 1400,
      top_p = 1,
      frequency_penalty = 0,
      presence_penalty = 0
    )

    text = response["choices"][0]["text"]
    while not text[0].isalpha():
        text = text[1::]
    return text

def get_short_url(url):
    if url is None:
        return
    short_url = None
    if "https://" in url:
        short_url = "https://"
        for i in range(8, len(url)):
            if url[i] != "/":
                short_url += url[i]
            else:
                break
        short_url += "/"
        
    if "http://" in url:
        short_url = "http://"
        for i in range(7, len(url)):
            if url[i] != "/":
                short_url += url[i]
            else:
                break
        short_url += "/"
    return short_url


def extract_domain(url):
    domain = re.findall(r'(?:https?://)?(?:www\.)?([^/]+)', url)
    return domain[0]
