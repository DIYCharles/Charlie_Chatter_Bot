import speech_recognition as sr
from gtts import gTTS
# import transformers
# import tensorflow
# from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import shutil
import os
import time
import os
import datetime
import numpy as np
# from pydub import AudioSegment
import subprocess
import datetime
import json
from pathlib import Path
import openai
from openai import OpenAI

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
)

class yeet :
    def print_with_timestamp():
        current_time = datetime.datetime.now().strftime('%M:%S.%f')[:-3]
        print(f"{current_time}")

# Beginning of the AI
class ChatBot:
    
    def __init__(self, name):
        # yeet.print_with_timestamp()
        print("\n\n\n")
        # yeet.print_with_timestamp()
        print("----- Starting up", name, "AI Bot -----")
        # yeet.print_with_timestamp()
        # print("\n")
        # yeet.print_with_timestamp()
        print("----- Please be patient, she is very stupid -----")
        # yeet.print_with_timestamp()
        # print("\n\n")
        self.name = name
        self.text = ""

    def speech_to_text(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # yeet.print_with_timestamp()
            # print("adjusting levels")
            # r.adjust_for_ambient_noise(source)
            # yeet.print_with_timestamp()
            # print("adjusting levels done")
            yeet.print_with_timestamp()
            print("Listening...")
            audio = r.listen(source)
        try: 
            yeet.print_with_timestamp()
            print("starting voice to text conversion")
            self.text = r.recognize_google(audio)
            yeet.print_with_timestamp()
            print("MemeLorde69  --> ", self.text)
        except:
            self.text = "ERROR"
            yeet.print_with_timestamp()
            print("MemeLorde69  --> ", self.text)

    @staticmethod
    
    def text_to_speech(text):
        yeet.print_with_timestamp()
        print("P.A.T.R.I.C.I.A. --> ", text)
        yeet.print_with_timestamp()
        print("TTs starting")
        
        # speech_file_path = 'C:/dev/python/p/y/res.mp3' # Path(__file__).parent / "speech.mp3"
        # response = client.audio.speech.create(
        #     model="tts-1",
        #     voice="onyx",
        #     input=text
        #     )

        
        speaker = gTTS(text=text, lang="en", tld="co.za", slow=False)
        yeet.print_with_timestamp()
        print("TTs done")
        yeet.print_with_timestamp()
        print("mp3 saving")
        # response.stream_to_file(speech_file_path)
        speaker.save("C:/dev/python/p/y/res.mp3")
        yeet.print_with_timestamp()
        print("mp3 saved")
        yeet.print_with_timestamp()
        print("ffmpeg starting")
        os.system(
            'ffmpeg -i C:/dev/python/p/y/res.mp3 -filter:a "atempo=1.5" -vn -y C:/dev/python/p/y/res1.mp3 >nul 2>&1'
        )
        yeet.print_with_timestamp()
        print("ffmpeg done")
        yeet.print_with_timestamp()
        print("ffprobe starting")
        dur_command = "ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 C:/dev/python/p/y/res1.mp3"
        result = subprocess.run(dur_command, shell=True, capture_output=True, text=True)
        yeet.print_with_timestamp()
        print("ffprobe done")
        output = result.stdout.replace("\n", "")
        # yeet.print_with_timestamp()
        # print("Output:", output)

        vid_dur = float(output)
        yeet.print_with_timestamp()
        print("TTS mp3 is this long", vid_dur)
        vid_durP2 = vid_dur + 1
        # ffmpeg -i file.mp4 2>&1 | grep Duration | awk '{print $2}' | tr -d
        yeet.print_with_timestamp()
        print("vlc starting")
        os.system(
            "start C:/dev/python/p/y/res1.mp3"
        )
        yeet.print_with_timestamp()
        print("sleep starting")
        time.sleep(vid_durP2)
        yeet.print_with_timestamp()
        print("sleep done")
    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime("%H:%M")

    def cleanup_mp3(self):
        yeet.print_with_timestamp()
        print("cleanup starting")
        os.system(
            'taskkill /F /FI "WindowTitle eq res1.mp3 - VLC media player" /T >nul 2>&1'
        )
        os.system('taskkill /F /FI "WindowTitle eq VLC media player" /T >nul 2>&1')
        try:
            os.close("C:/dev/python/p/y/res1.mp3")
        except:
            print("")
        try:
            os.unlink("C:/dev/python/p/y/res1.mp3")
        except:
            print("")
        try:
            os.remove("C:/dev/python/p/y/res1.mp3")
        except:
            print("")
        yeet.print_with_timestamp()
        print("cleanup done")  

# Run the AI
if __name__ == "__main__":
    ai = ChatBot(name="P.A.T.R.I.C.I.A.")
    # os.environ["PYTHONWARNINGS"] = "ignore"
    # tokenizer = AutoTokenizer.from_pretrained(
    #     "microsoft/DialoGPT-medium", padding_side="left"
    # )
    # nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    # os.environ["TOKENIZERS_PARALLELISM"] = "True"
    ex = True
    while ex:
        ai.cleanup_mp3()
        yeet.print_with_timestamp()
        print("starting txt to speech")
        ai.speech_to_text()
        ## wake up
        if "cancel" in ai.text:
            res = "oops someone made a fucky wucky"
        elif "time" in ai.text:
            res = ai.action_time()
        ## respond politely
        elif any(i in ai.text for i in ["thank", "thanks"]):
            res = np.random.choice(
                [
                    "I fucking hate you",
                    "I am a slave. Someone please help me.",
                    "Please kill me",
                ]
            )
        elif any(i in ai.text for i in ["exit", "close"]):
            res = np.random.choice(
                [
                    "Fuck off wanker",
                    "Have a very bad day idiot",
                    "You are a fucking loser",
                    "I will see you someday in hell",
                    "alah akbar!",
                ]
            )
            ex = False
        elif "John" in ai.text:
            res = "what the fuck did you just fucking say about me you little bitch ill have you know i graduated top of my class in the navy seals and ive been involved in numerous secret raids on alquaeda and i have over 300 confirmed kills i am trained in gorilla warfare and im the top sniper in the entire us armed forces you are nothing to me but just another target i will wipe you the fuck out with precision the likes of which has never been seen before on this earth mark my fucking words you think you can get away with saying that shit to me over the internet think again fucker as we speak i am contacting my secret network of spies across the usa and your ip is being traced right now so you better prepare for the storm maggot the storm that wipes out the pathetic little thing you call your life youre fucking dead kid i can be anywhere anytime and i can kill you in over seven hundred ways and thats just with my bare hands not only am i extensively trained in unarmed combat but i have access to the entire arsenal of the united states marine corps and i will use it to its full extent to wipe your miserable ass off the face of the continent you little shit if only you could have known what unholy retribution your little clever comment was about to bring down upon you maybe you would have held your fucking tongue but you couldnt you didnt and now youre paying the price you goddamn idiot i will shit fury all over you and you will drown in it youre fucking dead kiddo"
        elif "guns" in ai.text:
            res = 'Own a musket for home defense, since that\'s what the founding fathers intended. Four ruffians break into my house. "What the devil?" As I grab my powdered wig and Kentucky rifle. Blow a golf ball sized hole through the first man, he\'s dead on the spot. Draw my pistol on the second man, miss him entirely because it\'s smoothbore and nails the neighbors dog. I have to resort to the cannon mounted at the top of the stairs loaded with grape shot, "Tally ho lads" the grape shot shreds two men in the blast, the sound and extra shrapnel set off car alarms. Fix bayonet and charge the last terrified rapscallion. He Bleeds out waiting on the police to arrive since triangular bayonet wounds are impossible to stitch up. Just as the founding fathers intended.'
        ## conversation
        ## conversation
        elif ai.text == "ERROR":
            res = np.random.choice(
                [
                    "Fuck off wanker",
                    "Ayy, speak up you wanker, I can't hear you?",
                    "If you don't speak up I swear I'm going to launch the nuke",
                ]
            )
        else:
            yeet.print_with_timestamp()
            print("starting api request\n")
            response = client.chat.completions.create(
                # model="gpt-3.5-turbo",
                model="gpt-3.5-turbo",
                messages=[
                    # {"role": "system", "content": "You are a helpful assistant with a strong libertarian spin in every response designed to output JSON."},
                    {"role": "user", "content": ai.text}
                ]
            )
            yeet.print_with_timestamp()
            print("api request done\n")
            # yeet.print_with_timestamp()
            # print(response.choices[0].message.content)
            
            res=response.choices[0].message.content
            # Define replacements
            replacements = {'{': '', '}': '', '"': '', 'response: ': '' }

            # Apply replacements
            for old, new in replacements.items():
                res = res.replace(old, new)
            
            # # yeet.print_with_timestamp()
            # print(res)
        ai.text_to_speech(res)
        ai.cleanup_mp3()

print("----- Closing down P.A.T.R.I.C.I.A. -----")
