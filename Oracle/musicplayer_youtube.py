import webbrowser
import urllib2
def musicmain():
        print("-------------\n YOUTUBE MUSIC PLAYER\n GITHUB FOR THIS PROJECT (NOT MINE):\n https://github.com/retikulum/Python---Youtube-Music-Player/blob/master/Youtube_music_player.py-------------")
        user_want=raw_input("What do you want me to play?\n")
        #Replace spaces with + because YouTube searchs this way.
        user_want = user_want.replace(" ", "+")
        youtube_link="https://www.youtube.com/results?search_query=%s" % (user_want)
        print('Playing ' + user_want +', this may take a moment')
        #view source code
        request=urllib2.Request(youtube_link)
        response=urllib2.urlopen(request)
        ans=response.readlines()
        #find wacth?v= in source code then program open first video in search page
        for item in ans:
                if "watch?v=" in item:
                    a= item[item.index("watch?v="):]
                    break
        youtube="https://www.youtube.com/"+a[0:19]
        webbrowser.open_new_tab(youtube)
