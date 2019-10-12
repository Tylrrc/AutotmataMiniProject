#TODO: Adjust search pattern for getName to exclude titles (Dr., Mr., etc...)
#TODO: Implement ability to search by netID(will need to pull from web) AND html file
#TODO: Try regex patterns with something other than lazy quantifier

import sys
import re

if __name__ == '__main__':
    #print("\nPlease enter a URL or filename: \n")

    #input = sys.argv[1]

    file = open("Department of Computer Science - Dr. Byron Gao.html",'r')
    fileText = file.read()

    searchableString = re.sub(r"\s+", " ", fileText)

    # *******      Computer Science - (.*?)</title>
    # will return name!
    getName = re.search('Computer Science - (.*?)</title>',searchableString)
    name = getName.group(1)
    print("\nName: \t\t\t" + name)
    print()

    getEdu = re.search('Education</h3> </div> <div class="panel-body"><p>(.*?)</p>',searchableString)
    edu = getEdu.group(1)
    print("Education: \t\t" + edu)
    print()

    getRsch = re.search('Research Interests</h3> </div> <div class="panel-body"><p>(.*?)</p>',searchableString)
    rsch = getRsch.group(1)
    print("Research Interests: \t" + rsch)
    print()

    getUID = re.search('profiles/(.*?)/\">Login',searchableString)
    UID = getUID.group(1)
    print("Email: \t\t\t" + UID + "@txstate.edu")
    print()

    getWebpage = re.search('</h2> <h3><a target=\"_blank\" href=\"(.*?)\">Homepage', searchableString)
    webpage = getWebpage.group(1)
    print("Webpage: \t\t" + webpage)
    print()


    file.close()




