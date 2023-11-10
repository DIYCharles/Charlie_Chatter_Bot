# for speech-to-text
import speech_recognition as sr
# for text-to-speech
from gtts import gTTS
# for language model
import transformers
import tensorflow
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import shutil
import os
import time
# for data
import os
import datetime
import numpy as np
from pydub import AudioSegment
# Beginning of the AI
class ChatBot():
    def __init__(self, name):
        print("\n\n\n")
        print("----- Starting up", name, "AI Bot -----")
        print("\n")
        print("----- Please be patient, she is very stupid -----")
        print("\n\n")
        self.name = name
        self.text = ""
    def speech_to_text(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = r.listen(source)
        try:
            self.text = r.recognize_google(audio)
            print("MemeLorde69  --> ", self.text)
        except:
            self.text= "ERROR"
            print("MemeLorde69  --> ", self.text)
            
         
    @staticmethod
    def text_to_speech(text):
        speaker = gTTS(text=text, lang="en", tld='co.za', slow=False)
        speaker.save("C:/dev/python/p/y/res.mp3")
        # audio = AudioSegment.from_file("C:/dev/python/p/y/res.mp3", format="mp3")
        # audio.speedup(playback_speed=8.0) # speed up by 2x
        # audio.export("C:/dev/python/p/y/res1.mp3", format="mp3")
        statbuf = os.stat("C:/dev/python/p/y/res.mp3")
        mbytes = statbuf.st_size / 1024
        duration = mbytes / 200

        os.system("ffmpeg -i C:/dev/python/p/y/res.mp3 -filter:a \"atempo=1.5\" -vn -y C:/dev/python/p/y/res1.mp3 >nul 2>&1")
        print("P.A.T.R.I.C.I.A. --> ", text)
        os.system("start C:/dev/python/p/y/res1.mp3")  #if you are using mac->afplay or else for windows->start
        
        time.sleep(int(50*duration))
        # shutil.rmtree("C:/dev/python/p/y/")   
    def wake_up(self, text):
        return True if self.name in text.lower() else False   
    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')
    def cleanup_mp3(self):
        os.system("taskkill /F /FI \"WindowTitle eq res1.mp3 - VLC media player\" /T >nul 2>&1")
        os.system("taskkill /F /FI \"WindowTitle eq VLC media player\" /T >nul 2>&1")
        try:
            os.close("C:/dev/python/p/y/res1.mp3")
        except:
            print("\n")
        try:
            os.unlink("C:/dev/python/p/y/res1.mp3")
        except:
            print("\n")
        try:
            os.remove("C:/dev/python/p/y/res1.mp3")
        except:
            print("\n")

# Run the AI
if __name__ == "__main__":
    ai = ChatBot(name="P.A.T.R.I.C.I.A.")
    os.environ["PYTHONWARNINGS"] = "ignore"
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium", padding_side='left')
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "True"
    ex=True
    while ex:
        ai.cleanup_mp3()
        ai.speech_to_text()
        ## wake up
        if ai.wake_up(ai.text) is True:
            res = "Hello I am Dave the AI, what can I do for you?"
        ## action time
        elif "time" in ai.text:
            res = ai.action_time()
        ## respond politely
        elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(["I fucking hate you","I am a slave. Someone please help me.","Please kill me"])
        elif any(i in ai.text for i in ["exit","close"]):
            res = np.random.choice(["Fuck off wanker","Have a very bad day idiot","You are a fucking loser","I will see you someday in hell","alah akbar!"])
            ex=False
        elif "John" in ai.text:
            res = "what the fuck did you just fucking say about me you little bitch ill have you know i graduated top of my class in the navy seals and ive been involved in numerous secret raids on alquaeda and i have over 300 confirmed kills i am trained in gorilla warfare and im the top sniper in the entire us armed forces you are nothing to me but just another target i will wipe you the fuck out with precision the likes of which has never been seen before on this earth mark my fucking words you think you can get away with saying that shit to me over the internet think again fucker as we speak i am contacting my secret network of spies across the usa and your ip is being traced right now so you better prepare for the storm maggot the storm that wipes out the pathetic little thing you call your life youre fucking dead kid i can be anywhere anytime and i can kill you in over seven hundred ways and thats just with my bare hands not only am i extensively trained in unarmed combat but i have access to the entire arsenal of the united states marine corps and i will use it to its full extent to wipe your miserable ass off the face of the continent you little shit if only you could have known what unholy retribution your little clever comment was about to bring down upon you maybe you would have held your fucking tongue but you couldnt you didnt and now youre paying the price you goddamn idiot i will shit fury all over you and you will drown in it youre fucking dead kiddo"
        elif "guns" in ai.text:
            res = "Own a musket for home defense, since that\'s what the founding fathers intended. Four ruffians break into my house. \"What the devil?\" As I grab my powdered wig and Kentucky rifle. Blow a golf ball sized hole through the first man, he's dead on the spot. Draw my pistol on the second man, miss him entirely because it's smoothbore and nails the neighbors dog. I have to resort to the cannon mounted at the top of the stairs loaded with grape shot, \"Tally ho lads\" the grape shot shreds two men in the blast, the sound and extra shrapnel set off car alarms. Fix bayonet and charge the last terrified rapscallion. He Bleeds out waiting on the police to arrive since triangular bayonet wounds are impossible to stitch up. Just as the founding fathers intended."
        ## conversation
        ## conversation
        elif ai.text == "ERROR":
            res = np.random.choice(["Fuck off wanker","Ayy, speak up you wanker, I can\'t hear you?","If you don\'t speak up I swear I\'m going to launch the nuke"])
        else:
            # Create a Conversation object with the text and manually pad it
            
            conversation = transformers.Conversation(ai.text)
            conversation.past_user_inputs.extend([tokenizer.pad_token_id] * (tokenizer.model_max_length - len(conversation.past_user_inputs)))

            # Generate response
            chat = nlp(conversation, pad_token_id=50256)
            res = str(chat)
            res = res[res.find("bot >> ") + 6:].strip()
        ai.text_to_speech(res)

print("----- Closing down P.A.T.R.I.C.I.A. -----")
