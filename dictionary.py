import requests
from pprint import pprint


# word = 'hdasdhasgj'
# url = f'https://dictionaryapi.com/api/v3/references/learners/json/{word}?key=874e6bc2-61a2-408e-bb6e-4e7d8f336c8a'
learn_key = '874e6bc2-61a2-408e-bb6e-4e7d8f336c8a'
medical_key = 'd4e3d002-7222-4450-aaa1-a7bf96166ffe'


# r = requests.get(url)
# # pprint((r.status_code))
# res = r.json()
# sound = res[0]['hwi']['prs'][0]['sound']['audio']
# audio = f'https://media.merriam-webster.com/audio/prons/en/uk/mp3/{sound[0]}/{sound}.mp3'
# pprint(res)
#
# pprint(audio)
#
def getdef(word):
    url = f'https://dictionaryapi.com/api/v3/references/learners/json/{word}?key={learn_key}'
    r = requests.get(url)
    res = r.json()
    output = {}
    if not res:
        return False
    elif type(res[0]) == str:
        return False
    defs = res[0]['meta']['app-shortdef']['def']
    output['defs'] = "\n".join(defs)
    if res[0]['hwi']['prs'][0].get('sound'):
        sound = res[0]['hwi']['prs'][0]['sound']['audio']
        output['sound'] = f'https://media.merriam-webster.com/audio/prons/en/us/mp3/{sound[0].lower()}/{sound}.mp3'

    return output

# if __name__ == '__main__':
#     from pprint import pprint
#     pprint(getdef('taj'))
#     pprint(getdef('Uzbekistan'))
# pprint(getdef('hair'))
# pprint(getdef('tube'))
