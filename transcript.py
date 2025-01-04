from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# Download necessary datasets
nltk.download('punkt')
nltk.download('stopwords')

video_id = '<video_code_from_url>'
transcipt = YouTubeTranscriptApi.get_transcript(video_id)
# refer to notes(id1)
transcript_text = ' '.join([entry['text'] for entry in transcipt])
# print(transcipt_text)


# Function to process chunks of text
def process_text_in_chunks(text, chunk_size=5000):
    stop_words = set(stopwords.words('english'))
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    
    processed_text = []
    for chunk in chunks:
        sentences = sent_tokenize(chunk)
        filtered_sentences = []
        for sentence in sentences:
            words = word_tokenize(sentence)
            filtered_sentence = ' '.join([word for word in words if word.lower() not in stop_words])
            filtered_sentences.append(filtered_sentence)
        processed_text.append(' '.join(filtered_sentences))
    
    return ' '.join(processed_text)

# Process the large transcript
preprocessed_text = process_text_in_chunks(transcript_text)
print(len(preprocessed_text))  


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
            {"role": "user", "content": f"Based on the following transcript, answer the question:\n\nTranscript:\n{preprocessed_text}\n\nQuestion: {question}"}
        ],
        # refer to notes(id2)
        # max_tokens=200
    )

    return completion.choices[0].message.content

n = int(input("Enter number of questions you want to ask: "))
for i in range(n):
    question = input("Enter your query: ")
    answer = ans_ques(preprocessed_text, question)
    print(answer)
