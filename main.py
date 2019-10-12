#TODO: Adjust search pattern for getName to exclude titles (Dr., Mr., etc...)
#TODO: Try regex patterns with something other than lazy quantifier (YOU LAZY @#&$!)
#TODO: Send output to file, not just console

import re
import requests

if __name__ == '__main__':

    print("\n****** CS Faculty Lookup ******\n")

    print("Enter either a: \n")
    print("\t- netID, or\n")
    print("\t- a path to a *.html file downloaded from http://www.cs.txstate.edu/Personnel/Faculty\n")

    input = input('---> ')
    isHTMLFile = True

    if (re.search('.html$', input)):
        file = open(input,'r')
        fileText = file.read()
    else:
        url = 'http://www.cs.txstate.edu/Personnel/' + input
        fileText = requests.get(url).text
        isHTMLFile = False

    searchableString = re.sub(r"\s+", " ", fileText)

    getName = re.search('Computer Science - (.*?)</title>',searchableString)
    try:
        name = getName.group(1)
    except AttributeError:
        name = "Not Found"
    print("\nName: \t\t\t" + name)
    print()

    getEdu = re.search('Education</h3> </div> <div class="panel-body"><p>(.*?)</p>',searchableString)

    try:
        edu = getEdu.group(1)
    except AttributeError:
        edu = "Not Found"

    print("Education: \t\t" + edu)
    print()

    getRsch = re.search('Research Interests</h3> </div> <div class="panel-body"><p>(.*?)</p>',searchableString)

    try:
        rsch = getRsch.group(1)
    except AttributeError:
        rsch = "Not Found"

    print("Research Interests: \t" + rsch)
    print()

    getUID = re.search('profiles/(.*?)/\">Login',searchableString)

    try:
        UID = getUID.group(1)
    except AttributeError:
        UID = "Not Found"
    print("Email: \t\t\t" + UID + "@txstate.edu")
    print()

    getWebpage = re.search('</h2> <h3><a target=\"_blank\" href=\"(.*?)\">Homepage', searchableString)

    try:
        webpage = getWebpage.group(1)
    except AttributeError:
        webpage = "Not Found"
    print("Webpage: \t\t" + webpage)
    print()

    if isHTMLFile:
        file.close()




