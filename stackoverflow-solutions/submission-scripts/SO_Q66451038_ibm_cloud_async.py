
"""
Purpose: stackoverflow answer
Date created: 2021-03-05

Title: How can I bulk/batch transcribe wav files using python?
URL: https://stackoverflow.com/questions/66451038/how-can-i-bulk-batch-transcribe-wav-files-using-python

Contributor(s):
    Mark M.
"""

# https://github.com/freelanceastro/interview-transcriber/tree/master/examples/obama-shell

# https://obamawhitehouse.archives.gov/realitycheck/blog/2015/07/11/weekly-address-making-our-communities-stronger-through-fair-housing

# Folder C:\Users\Work1\Desktop\Info\PythonFiles\watson-files\obama
# curl -o "080815_WeeklyAddress.mp4" "https://obamawhitehouse.archives.gov/WeeklyAddress/2015/080815-RGDPSW/080815_WeeklyAddress.mp4"
# curl -o "071115_WeeklyAddress.mp4" "https://obamawhitehouse.archives.gov/WeeklyAddress/2015/071115-DRGDSP/071115_WeeklyAddress.mp4"

# ffmpeg
# ffmpeg -i "080815_WeeklyAddress.mp4" -vn -ar 16000 -acodec pcm_s16le "080815_WeeklyAddress.wav"
# ffmpeg -i "071115_WeeklyAddress.mp4" -vn -ar 16000 -acodec pcm_s16le "071115_WeeklyAddress.wav"

"""
{
  "apikey": "qbj74s_9YAMjt31Lfp-HepAyEoZeVcahneHQmLG9Ik__",
  "iam_apikey_description": "Auto-generated for key c7f12a08-7a87-43cd-a7cb-86f89880f81a",
  "iam_apikey_name": "Auto-generated service credentials",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/64edba771fbc4e7da12c29bd0c01c00b::serviceid:ServiceId-f3f0b25e-994a-4045-a779-20af58b35fc9",
  "url": "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/726a9204-ea75-4bb7-9d27-90c0bf57e5db"
}


curl -X POST ^
     -u "apikey:qbj74s_9YAMjt31Lfp-HepAyEoZeVcahneHQmLG9Ik__" ^
     -o 080815_WeeklyAddress.json ^
     -H "Content-Type: audio/wav" ^
     -H "Transfer-Encoding: chunked" ^
     --data-binary "@080815_WeeklyAddress.wav" ^
     "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?continuous=true&timestamps=true&word_confidence=true&profanity_filter=false"

curl -X POST ^
     -u "apikey:qbj74s_9YAMjt31Lfp-HepAyEoZeVcahneHQmLG9Ik__" ^
     -o 071115_WeeklyAddress.json ^
     -H "Content-Type: audio/wav" ^
     -H "Transfer-Encoding: chunked" ^
     --data-binary "@071115_WeeklyAddress.wav" ^
     "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?continuous=true&timestamps=true&word_confidence=true&profanity_filter=false"

"""

####RUN THIS PART FIRST#########
import os
import json
import time
# import threading
from pathlib import Path

import asyncio
import concurrent.futures

# from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import pandas as pd

my_api_key = "qbj74s_9YAMjt31Lfp-HepAyEoZeVcahneHQmLG9Ik__"
directory = Path(r"C:\Users\Work1\Desktop\Info\PythonFiles\watson-files\obama")

# list(directory.glob("**/*.wav"))
# audio_file_path = directory.joinpath("080815_WeeklyAddress.wav")

authenticator = IAMAuthenticator(my_api_key)

service = SpeechToTextV1(authenticator=authenticator)
# service.set_service_url('https://api.us-east.speech-to-text.watson.cloud.ibm.com')
service.set_service_url('https://stream.watsonplatform.net/speech-to-text/api')


models = service.list_models().get_result()
#print(json.dumps(models, indent=2))

model = service.get_model('en-US_BroadbandModel').get_result()
#print(json.dumps(model, indent=2))



# get data to a csv
########################RUN THIS PART SECOND#####################################


def process_data(json_data, output_path):

    print(f"Processing: {output_path.stem}")

    cols = ["transcript", "confidence"]

    dfdata = [[t[cols[0]], t[cols[1]]] for r in json_data.get('results') for t in r.get("alternatives")]

    df0 = pd.DataFrame(data = dfdata, columns = cols)

    df1 = pd.DataFrame(json_data.get("speaker_labels")).drop(["final", "confidence"], axis=1)


    # test3 = pd.concat([df0, df1], axis=1)
    test3 = pd.merge(df0, df1, left_index = True, right_index = True)


    # sentiment
    print(f"Getting sentiment for: {output_path.stem}")
    transcript = test3["transcript"]
    transcript.dropna(inplace=True)

    analyzer = SentimentIntensityAnalyzer()
    text = transcript
    scores = [analyzer.polarity_scores(txt) for txt in text]

    # data = pd.DataFrame(text, columns = ["Text"])
    data = transcript.to_frame(name="Text")
    data2 = pd.DataFrame(scores)


    # final_dataset= pd.concat([data, data2], axis=1)
    final_dataset = pd.merge(data, data2, left_index = True, right_index = True)

    # test4 = pd.concat([test3, final_dataset], axis=1)
    test4 = pd.merge(test3, final_dataset, left_index = True, right_index = True)

    test4.drop("Text", axis=1, inplace=True)

    test4.rename(columns = {
            "neg": "Negative",
            "pos": "Positive",
            "neu": "Neutral",
            }, inplace=True)

    # This is the name of the output csv file
    test4.to_csv(output_path, index = False)




def process_audio_file(filename, output_type = "csv"):

    audio_file_path = directory.joinpath(filename)

    # Update output path to consider output_type parameter.
    out_path = directory.joinpath(f"{audio_file_path.stem}.{output_type}")

    print(f"Current file: '{filename}'")

    with open(audio_file_path, "rb") as audio_file:
        data = service.recognize(
                audio = audio_file,
                speaker_labels = True,
                content_type = "audio/wav",
                inactivity_timeout = -1,
                model = "en-US_NarrowbandModel",
                continuous = True,
            ).get_result()

    print(f"Speech-to-text complete for: '{filename}'")

    return [data, out_path]
    # process_data(res, out_file_path)


# async def main():
#     print("Running main()...")

#     tasks = [asyncio.create_task(process_audio_file(f)) for f in directory.glob("**/*.wav")]

#     await asyncio.gather(*tasks)

def main():
    print("Running main()...")

    n_workers = os.cpu_count() + 2

    file_gen = directory.glob("**/*.wav")
    with concurrent.futures.ThreadPoolExecutor(max_workers = n_workers) as executor:
        futures = {executor.submit(process_audio_file, f) for f in file_gen}
        for future in concurrent.futures.as_completed(futures):
            pkg = future.result()
            process_data(*pkg)


if __name__ == "__main__":
    print(f"Program to process audio files has started.")
    t_start = time.perf_counter()

    # looper = asyncio.get_event_loop()
    # looper.run_until_complete(main())

    # asyncio.run(main())

    main()

    # looper.close()
    t_stop = time.perf_counter()
    print(f"Done! Processing completed in {t_stop - t_start} seconds.")


# $ python SO_Q66451038_ibm_cloud_multi_file.py

# ####RUN THIS PART FIRST#########
# import json
# from os.path import join, dirname
# from ibm_watson import SpeechToTextV1
# from ibm_watson.websocket import RecognizeCallback, AudioSource
# import threading
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# import pandas as pd
# authenticator = IAMAuthenticator('xxyyzz')

# service = SpeechToTextV1(authenticator=authenticator)
# service.set_service_url('https://api.us-east.speech-to-text.watson.cloud.ibm.com')

# models = service.list_models().get_result()
# #print(json.dumps(models, indent=2))

# model = service.get_model('en-US_BroadbandModel').get_result()
# #print(json.dumps(model, indent=2))

# # This is the name of the file u need to change below
# with open(join(dirname('__file__'), 'Call 8.wav'),
#           'rb') as audio_file:
# #    print(json.dumps(
#     output = service.recognize(
#     audio=audio_file,
#     speaker_labels=True,
#     content_type='audio/wav',
#     #timestamps=True,
#     #word_confidence=True,
#     inactivity_timeout = -1,
#     model='en-US_NarrowbandModel',
#     continuous=True).get_result(),
#     indent=2
#   ############END################################  

# # get data to a csv
# ########################RUN THIS PART SECOND#####################################
# df0 = pd.DataFrame([i for elts in output for alts in elts['results'] for i in alts['alternatives']])

# df1 = pd.DataFrame([i for elts in output for i in elts['speaker_labels']])

# list(df0.columns) 
# list(df1.columns) 
# df0 = df0.drop(["timestamps"], axis=1)
# df1 = df1.drop(["final"], axis=1)
# df1 = df1.drop(['confidence'],axis=1)
# test3 = pd.concat([df0, df1], axis=1)
# #sentiment
# transcript = test3['transcript']
# transcript = transcript.dropna()
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# analyzer = SentimentIntensityAnalyzer()
# text = transcript
# scores = []
# for txt in text:
#     vs = analyzer.polarity_scores(txt)
#     scores.append(vs)
# data = pd.DataFrame(text, columns= ['Text'])
# data2 = pd.DataFrame(scores)
# final_dataset= pd.concat([data,data2], axis=1)
# test4 = pd.concat([test3,final_dataset], axis=1)
# test4 = test4.drop(['Text'],axis=1)
# test4.rename(columns={'neg':'Negative'}, 
#                  inplace=True)
# test4.rename(columns={'pos':'Positive'}, 
#                  inplace=True)
# test4.rename(columns={'neu':'Neutral'}, 
#                  inplace=True)

# # This is the name of the output csv file
# test4.to_csv("Call 8.csv")