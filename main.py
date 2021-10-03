import requests, time, os

url = input('url (add https:// or http://) >: ')
delay = input('delay amount (in seconds) >: )

if url == url :  # stops the code from running before user input is typed
    if delay == delay :  # same as above
        while True :  # forever
            r = requests.get(url)  # request the page
            f = open("temp.txt", "w+")  # open temp.txt
            f.write(r.text)  # write in what it got from the page (r.text)
            f.delete("temp.txt") # idk how to code
            print(f'Pinged {url} with status code {r.status_code} | Uptimer v1')  # displays a simple message 
            time.sleep(int(delay))  # waits (delay) seconds then repeats
