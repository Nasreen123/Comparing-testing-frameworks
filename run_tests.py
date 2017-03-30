
import json
from subprocess import Popen, PIPE

def get_test_feedback(url, result_path):
    #generate filename to use from the url
    start = url.find("//") + 2
    end = url.find("/", start)
    name = url[start:end]
    filename = name + ".json" #url[11:19] + ".json"
    print(filename)

    #call to pa11y tool
    process = Popen(["pa11y", "--reporter", "json", url], stdout=PIPE, stderr=PIPE) #"pa11y", url)

    #get result and error
    output, error = process.communicate()
    if error:
        print("ERROR: ", error)

    #save result as json file
    with open(result_path + filename, 'w') as outfile:
        json.dump(output, outfile)

def get_urls():
    f = open("urls.txt", 'r')
    string = str(f.read())
    f.close()
    urls = string.split()
    return urls

urls = get_urls()

result_path = "pa11y/"

for url in urls:
    get_test_feedback(url, result_path)
