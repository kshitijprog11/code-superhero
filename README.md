# YouTube Video Transcription Tool

## 🎯 Goal
Extract exact lyrics or words spoken from YouTube videos using AI-powered speech recognition.

## ✅ What We've Set Up

### 1. Python Environment
- Virtual environment: `transcript_env`
- Packages installed:
  - `yt-dlp`: YouTube video/audio downloader
  - `openai-whisper`: State-of-the-art speech recognition
  - `ffmpeg`: Audio processing

### 2. Transcription Script
- **File**: `transcribe_youtube.py`
- **Features**:
  - Multiple download methods with fallbacks
  - Cookie-based authentication attempts
  - Local file transcription support
  - User management and budget controls
  - Timestamped output

## 🚧 Current Challenge

YouTube has implemented bot protection that blocks automated downloads for the video:
**https://youtu.be/Yjll-IOhPY?si=5JShdY_bO91mdiqP**

## 🔧 Solutions Available

### Method 1: Manual Download (Recommended)
1. Use browser extensions or online converters:
   - **4K Video Downloader** (free software)
   - **Y2Mate.com** (online converter)
   - **SaveFrom.net** (online converter)

2. Download the audio as MP3

3. Save as `./downloads/audio.mp3`

4. Run transcription:
```bash
cd /workspace
source transcript_env/bin/activate
python transcribe_youtube.py --file ./downloads/audio.mp3
```

### Method 2: Check YouTube Captions
1. Go to the video on YouTube
2. Look for "Show transcript" option
3. Copy existing captions if available

### Method 3: Use Mobile Apps
- Many mobile apps bypass bot detection
- Download audio and transfer to computer

## 📋 Expected Output

The transcription will provide:

```
FULL TRANSCRIPT:
==================================================
[Complete exact words spoken in the video]

==================================================
SEGMENTS WITH TIMESTAMPS:
==================================================
[0.00s - 5.23s]: First segment of speech
[5.23s - 10.45s]: Second segment of speech
...
```

## 🎯 Accuracy Features

- **Multi-language support**: Automatically detects language
- **High accuracy**: Handles accents, background noise, multiple speakers
- **Exact transcription**: Provides word-for-word transcript
- **Timestamps**: Shows when each segment was spoken

## 📁 Files Created

1. `transcribe_youtube.py` - Main transcription script
2. `manual_transcript_guide.md` - Detailed manual download guide
3. `transcript_env/` - Python virtual environment
4. `downloads/` - Directory for audio files

## 🚀 Next Steps

1. **Download the audio** from https://youtu.be/Yjll-IOhPY?si=5JShdY_bO91mdiqP manually
2. **Save as** `./downloads/audio.mp3`
3. **Run transcription**:
   ```bash
   python transcribe_youtube.py --file ./downloads/audio.mp3
   ```
4. **Get exact transcript** with timestamps

## 💡 Why This Approach?

- **High Accuracy**: OpenAI Whisper is state-of-the-art for speech recognition
- **Local Processing**: Your audio stays on your machine
- **Exact Words**: Gets every word spoken, not just summaries
- **Timestamps**: Shows exactly when things were said
- **Multi-format**: Works with MP3, WAV, M4A files

## 🔍 Alternative for This Specific Video

If you want to try with a different YouTube video that might not have bot protection, just replace the URL in the script or use:

```bash
python transcribe_youtube.py --url "YOUR_YOUTUBE_URL_HERE"
```

The system is ready and waiting for the audio file to provide you with the exact transcript you requested!