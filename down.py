from pafy import new

url = input("enter you link here: ")
video = new(url)
dl = video.getbest()
dl.download()