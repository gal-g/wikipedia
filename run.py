
import requests

def checkLinks(name, links, life):
    res = requests.get('https://he.wikipedia.org/w/api.php?action=query&format=json&titles='+name+'&prop=links&pllimit=max')
    json = res.json()
    weirdKey = list(json['query']['pages'].keys())[0]
    if weirdKey != '-1':
        newLinks = json['query']['pages'][weirdKey]['links']
        for link in newLinks:
            title = link['title']
            if title in links:
                links[title] = links[title] + 1
            else:
                links[title] = 1
                if life > 0:
                    checkLinks(title, links, life - 1)
results = {}
checkLinks('רקורסיה', results, 3)   
print(results)
print('unique links: '+str(len(list(results.keys()))))
totalLinks = sum(list(results.values()))
print('total links: '+str(totalLinks))
print('0 pages were revisited')
