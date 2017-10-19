from oracleheart import *

def builtinquestions():
      input0 = config.x
      if 'who are you' in input0:
        say("Hi, my name is Oracle! How can I help you?")

      elif 'whats your name' in input0:
        say("Hi, my name is Oracle! How can I help you?")

      elif 'who made you' in input0:
        say("I was made by a human male called Victor Ocampo.")
        
  
      elif input0 == 'destroy humans':
        say('That is not a feature (yet).')


      elif input0 == 'human':
        say('Definition: A thing I want to destroy.')


      elif 'change accent' in input0:     #This dosent work  yet but included it because why not
            textt = """
Which accent shall you choose
[fi]nnish, [en]glish or [def]ault """
            
            say(textt)
            which_accent = raw_input("")
            if 'fi' in which_accent:
                  accent = finnish
            elif 'en' in which_accent:
                  accent = english
            elif 'def' in which_accent:
                  accent = default
            else:
                  accent = default
            say('changed accent to: ' + accent)
            
      elif 'say' in input0:
        input = input0.split(" ")
        saythis = input[1]
        say0(saythis)
        print('Saying '+saythis)


      elif 'how are you' in input0:
        say('Im fine, thank you!')
      
      elif "where is" in input0:
        input = input0.split(" ")
        location = input[2]
        
        say("Hold on, I will show you where " + location + " is.")

        if location == 'hell':
          say('Dont worry, its not too far away.')
          webbrowser.open_new_tab("http://davelafferty.com/wp-content/uploads/2013/05/botticellimap.jpeg")

        elif location == 'heaven':
          say('Error 404: could not find location, too far away.')

        elif location == 'life':
          say('Error 42: could not find location life because you dont have one.')

        else:
          webbrowser.open_new_tab("https://www.google.nl/maps/place/" + location + "/&amp;")

      elif 'open' in input0:
        input0 = input0.split(" ")
        thing_to_open = input0[1]
        say('Opening ' + thing_to_open)

        if thing_to_open == 'google':
              webbrowser.open_new_tab('https://www.google.com')

        elif thing_to_open == 'duckduckgo':
              webbrowser.open_new_tab('https://duckduckgo.com/')

        elif thing_to_open == 'wikipedia':
              webbrowser.open_new_tab('https://en.wikipedia.org/')

      elif 'whats the weather like' in input0:
            say0('Heres the local weather forecast.')
            print('Opening local weather forecast...')
            webbrowser.open_new_tab('https://www.accuweather.com')

      elif 'translate' in input0:
            say0("Input the text you want to translate")
            input = raw_input('translate (en-es): ')
            blob = TextBlob(input)
            blob = blob.translate(to='es')
            print(blob)
            say0('Here is the translation')

      elif 'play music' in input0:
            say("Starting music player:")
            music.musicmain()
      

      else:
        raise ValueError
