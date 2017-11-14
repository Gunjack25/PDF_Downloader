from urllib import request

def download(url_to_download, name):

    response = request.urlopen(url_to_download)
    ob = open(name, 'wb')
    url_download = ob.write(response.read())
    ob.close()
    print('Completed')

if __name__ == '__main__':
    url_to_download = input('Enter the url you want to be downloaded\t')
    name = input("What name do you want the file to have?\t")
    download(url_to_download, name)
