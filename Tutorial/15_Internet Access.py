import urllib2

link = "https://www.youtube.com"

def main():
    # open a connection to a URL using urllib2
    webUrl = urllib2.urlopen(link)

    # get the result code and print it
    print "result code: " + str(webUrl.getcode()), "\n\n"

    # read the data from the URL and print it
    data = webUrl.read()
    print data


if __name__ == "__main__":
    main()