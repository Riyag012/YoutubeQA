from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

video_id = '5zuF4Ys1eAw&t'
transcipt = YouTubeTranscriptApi.get_transcript(video_id)
# refer to notes(id1)
transcript_text = ' '.join([entry['text'] for entry in transcipt])
# print(transcipt_text)

API_KEY = "<Your_API_Key>"
client = OpenAI(
  api_key=API_KEY
)

def ans_ques(transcipt, question):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        # refer to notes(id3)
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Based on the following transcript, answer the question:\n\nTranscript:\n{transcript_text}\n\nQuestion: {question}"}
        ],
        # refer to notes(id2)
        max_tokens=50
    )

    return completion.choices[0].message.content

n = int(input("Enter number of questions you want to ask: "))
for i in range(n):
    question = input("Enter your query: ")
    answer = ans_ques(transcript_text, question)
    print(answer)
