import datetime
import speak
import webbrowser
import weather
import os




def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn :
      speak.speak("my name is virtual Assistant")  
      return "my name is virtual Assistant"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn: 
        speak.speak("Hey sir, How i can  help you !")  
        return "Hey sir, How i can  help you !" 

    elif "how are you" in  data_btn :
            speak.speak("I am doing great these days sir") 
            return "I am doing great these days sir"   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure sir to stay with you")
           return "its my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning Aditya , i think you might need some help")
           return "Good morning sir, i think you might need some help"   

    elif "time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("ok Aditya have nice day")
            return "ok sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")   
        speak.speak("gaana.com is now ready for you, enjoy your music")                   
        return "gaana.com is now ready for you, enjoy your music"


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    
    
    elif 'weather' in data_btn :
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..." 
    
    elif "hey" in data_btn :
        speak.speak("hi aditya ")
        return "hey Aditya"  
    

    else :
        url=f'https://www.google.com/search?q={data_btn}&sca_esv=60b997825705a04a&rlz=1C1CHBF_enIN977IN977&sxsrf=ACQVn08l2-nXg_b2Jf-nppMWjblMVz7CcQ%3A1712299176638&ei=qJwPZvbDJsHl2roP24aK2Aw&ved=0ahUKEwj2t7DBu6qFAxXBslYBHVuDAssQ4dUDCBA&uact=5&oq={data_btn}&gs_lp=Egxnd3Mtd2l6LXNlcnAiCWluc3RhZ3JhbTIKECMYgAQYigUYJzIKECMYgAQYigUYJzIKECMYgAQYigUYJzIREAAYgAQYigUYkQIYsQMYgwEyDhAAGIAEGIoFGJECGLEDMgsQABiABBiKBRiRAjIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzILEAAYgAQYsQMYgwEyChAAGIAEGIoFGENIhpYRUIHvEFjtkRFwA3gAkAEBmAHLBqABpDOqAQc0LTEuNi4zuAEDyAEA-AEBmAIMoAKqLagCFMICChAAGIAEGAoYsAPCAgcQABgeGLADwgIJEAAYCBgeGLADwgIHECMY6gIYJ8ICFhAAGAMYjwEY5QIY6gIYtAIYjAPYAQHCAhAQLhjHARjRAxiABBiKBRgnwgIREC4YgAQYigUYkQIYsQMYgwHCAg4QABiABBiKBRixAxiDAcICBRAAGIAEwgINEAAYgAQYigUYQxjJA8ICCxAAGIAEGIoFGJIDwgIQEC4YgAQYigUYQxjHARjRA8ICChAuGIAEGIoFGEPCAgoQLhhDGIAEGIoFwgIMEAAYgAQYigUYQxgKwgIIEAAYgAQYsQOYAw-IBgGQBgq6BgYIARABGAuSBwkzLjQtNC40LjGgB5d1&sclient=gws-wiz-serp'
        webbrowser.get().open(url)
        speak.speak( f' searching {data_btn} ')
        return f'{data_btn} open'      
