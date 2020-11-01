from ConsineSim import cosineSim
from apiclient.discovery import build

searchEngine_API = 'AIzaSyCUYy9AtdMUddiNA0gOcsGPQcE372ytyCw'
searchEngine_Id = '758ad3e78879f0e08'

def searchWeb(text,output,c):
    text = text
    # print(text)
    try:  
        resource = build("customsearch", 'v1', developerKey=searchEngine_API).cse()
        result = resource.list(q = text, cx = searchEngine_Id).execute()
        searchInfo = result['searchInformation']
        #print(searchInfo)
        if(int(searchInfo['totalResults']) > 0):
            item = result['items'][0]
            # print(item['snippet'])
            content = item['snippet']
            if(item['link'] in output):
                output[item['link']] = output[item['link']] + 1

                c[item['link']] = (c[item['link']]*(output[item['link']] - 1) + cosineSim(text,content))/(output[item['link']])
            else:
                output[item['link']] = 1
                c[item['link']] = cosineSim(text,content)
    except: 
        # print('error')
        return output,c
    return output,c
