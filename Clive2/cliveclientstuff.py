from cliveheart import *

spanish = 'es'
english = 'en'
french = 'fr'
current_lang =  english   #Change the wikipedia articles language here

wikipedia.set_lang(current_lang)

#wolframalpha API stuff
wolfram_app_id = secrets.wolfram_app_id
wolfram_client = wolframalpha.Client(wolfram_app_id)

#wordnick API stuff
APIurl_wordnick = secrets.APIurl_wordnick
APIKey_wordnick = secrets.APIKey_wordnick

wordnick_client = swagger.ApiClient(APIKey_wordnick, APIurl_wordnick)

wordApi = WordApi.WordApi(wordnick_client)
