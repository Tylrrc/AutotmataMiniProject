#TODO: Adjust search pattern for getName to exclude titles (Dr., Mr., etc...)
#TODO: Try regex patterns with something other than lazy quantifier (YOU LAZY @#&$!)

import re
import requests

if __name__ == '__main__':

    print("\n****** CS Faculty Lookup ******\n")

    print("Enter either: \n")
    print("\t- a CS Faculty netID, or\n")
    print("\t- a path to a *.html file downloaded from http://www.cs.txstate.edu/Personnel/Faculty\n")

    input = input('---> ')


    if (re.search('.html$', input)):
        infile = open(input,'r')
        fileText = infile.read()
        isHTMLFile = True
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


    getEdu = re.search('Education</h3> </div> <div class="panel-body"><p>(.*?)</p>',searchableString)

    try:
        edu = getEdu.group(1)
    except AttributeError:
        edu = "Not Found"


    getRsch = re.search('Research Interests</h3> </div> <div class="panel-body"><p>(.*?)</p>',searchableString)

    try:
        rsch = getRsch.group(1)
    except AttributeError:
        rsch = "Not Found"


    getUID = re.search('profiles/(.*?)/\">Login', searchableString)

    try:
        outfilePrefix = UID = getUID.group(1)
        UID = "Not Found" if name == "Not Found" else UID + "@txstate.edu"
    except AttributeError:
        UID = "Not Found"


    getWebpage = re.search('</h2> <h3><a target=\"_blank\" href=\"(.*?)\">Homepage', searchableString)

    try:
        webpage = getWebpage.group(1)
    except AttributeError:
        webpage = "Not Found"

    outfile = open(outfilePrefix + ".txt", "w+")


    print("\nName: \t\t\t" + name)
    print()
    print("Education: \t\t" + edu)
    print()
    print("Research Interests: \t" + rsch)
    print()
    print("Email: \t\t\t" + UID)
    print()
    print("Webpage: \t\t" + webpage)
    print()

    outfile.write("\nName: \t\t\t" + name + "\n\n")
    outfile.write("Education: \t\t" + edu + "\n\n")
    outfile.write("Research Interests: \t" + rsch + "\n\n")
    outfile.write("Email: \t\t\t" + UID + "\n\n")
    outfile.write("Webpage: \t\t" + webpage + "\n\n")


    outfile.close()

    if isHTMLFile:
        infile.close()




