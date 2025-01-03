# **YouTubeQA**

## **Overview**
YouTubeQA is a Python-based project that extracts transcripts from YouTube videos and allows users to ask questions based on the video's content. The project integrates
the YouTube Transcript API for extracting video transcripts and OpenAI's API for generating intelligent responses.

---

## **Contents**
1. [Features](#features)  
2. [Prerequisites](#prerequisites)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Example](#example)  
6. [Limitations](#limitations)  
7. [Future Enhancements](#future-enhancements) 

---

## **Features**
- Extracts subtitles/transcripts from YouTube videos with ease.  
- Uses OpenAI's GPT models to answer questions about the video content.  
- User-friendly interface to input video IDs and questions interactively.  

---

## **Prerequisites**
Before running the code, ensure you have:
1. **Python 3.8 or higher** installed.  
2. An **OpenAI API key**.  
3. The required Python libraries:  
   - `youtube-transcript-api`  
   - `openai`

---

## **Installation**

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/YouTubeQA.git
   cd YouTubeQA
   ```

2. **Install dependencies:**
   ```bash
   pip install youtube-transcript-api openai
   ```

3. **Set up your API key:**  
   Replace `<Your_API_Key>` in the script with your actual OpenAI API key.

---

## **Usage**

1. **Extract Transcripts:**  
   Provide the `video_id` from the YouTube URL.  
   - Example: For `https://www.youtube.com/watch?v=5zuF4Ys1eAw`, the `video_id` is `5zuF4Ys1eAw`.

2. **Run the Script:**  
   Execute the script using:
   ```bash
   python your_script_name.py
   ```

3. **Ask Questions:**  
   When prompted, input your question. The script will generate an answer based on the video's transcript.

---

## **Example**

**Input:**  
YouTube Video ID: `5zuF4Ys1eAw`  
Question: `What is the main topic of this video?`  

**Output:**  
*"The video provides the AI trends for 2025."*

---

## **Limitations**
1. The YouTube video must have subtitles (closed captions) available.  
2. The OpenAI API usage may incur costs.  
3. Long transcripts may require truncation due to API limits.  

---

## **Future Enhancements**
1. Add support for summarizing videos before answering questions.  
2. Implement support for videos in multiple languages.  
3. Enable batch processing of multiple questions.  

---
