from oracleheart import *

say("Welcome human, my name is Oracle")


def Main():
  input = raw_input("Q:  ")

  if input == '':
    say0('You did not enter a question')
    print('\n\n')

  else:
    print('\n\n')
    
    input = input.lower()

    originalinput = input #Trust me this is important

    config.x = input  #This creates a module wide variable variable

    try:
      personalquestions()
    
    except:
      try:
            #wordnick
            input = input.split(' ')
            input = " ".join(input[2:])

            answer = wordApi.getDefinitions(input, limit=1)

            say('Definition: ' + answer[0].text)
            print('\n(According to Wordnik https://www.wordnik.com/)\n')
      
      except:
          input = originalinput
          try:
              #wolframalpha
              res = wolfram_client.query(input)   
              answer = next(res.results).text
          
              say(answer)

          except:
                  #wikipedia
                  try:
                      input = input.split(' ')
                      input = " ".join(input[2:])
                      say(wikipedia.summary(input, sentences=2))

                      print('\n(According to Wikipedia, link: '+wikipedia.page(input).url+')')
                      
                  except:
                      say('Sorry, I did not understand!')
