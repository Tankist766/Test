import os

puti = []
def leh():
    for name in os.listdir('images'):
         put = f"images\{name}"
         puti.append(put)
    return puti

print(leh)


def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']