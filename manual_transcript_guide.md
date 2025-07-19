# Manual YouTube Video Transcription Guide

## When Automated Downloads Fail

YouTube has implemented bot protection that blocks automated downloads. Here are several methods to get the transcript:

## Method 1: Browser-Based Download (Recommended)

### Option A: Browser Extensions
1. **4K Video Downloader** (Free)
   - Install from: https://www.4kdownload.com/
   - Paste YouTube URL
   - Select audio only (MP3)
   - Download

2. **yt-dlp Browser Extension**
   - Install from Chrome/Firefox store
   - Click on extension while on YouTube video
   - Select audio format

### Option B: Online Converters
1. **Y2Mate.com**
2. **SaveFrom.net**
3. **OnlineVideoConverter.com**

**Steps:**
1. Go to: https://youtu.be/Yjll-IOhHPY?si=5JShdY_bO91mdiqP
2. Copy the URL
3. Paste into online converter
4. Select MP3/Audio format
5. Download the audio file

## Method 2: Check for Existing Captions

YouTube videos sometimes have auto-generated or manual captions:

1. Go to the YouTube video
2. Click on the "..." menu below the video
3. Select "Show transcript" if available
4. Copy the transcript text

## Method 3: Use Our Local Transcription

Once you have the audio file:

1. Save the audio file as `audio.mp3` in the `./downloads/` folder
2. Run our transcription script:

```bash
cd /workspace
source transcript_env/bin/activate
python transcribe_youtube.py --file ./downloads/audio.mp3
```

## Method 4: Alternative Tools

### WebPilot or Similar Services
- Some browser extensions can extract transcripts directly
- Search for "YouTube transcript extractor" in your browser's extension store

### Mobile Apps
- Many mobile apps can download YouTube audio without bot detection
- Transfer the file to your computer afterward

## The Transcription Process

Our Whisper-based transcription will provide:
- **Full transcript** with exact words spoken
- **Timestamped segments** showing when each part was said
- **High accuracy** even with accents, background noise, or multiple speakers

## Output Format

The transcript will be saved as `transcript.txt` with:

```
FULL TRANSCRIPT:
==================================================

[Complete transcript text here]

==================================================
SEGMENTS WITH TIMESTAMPS:
==================================================

[0.00s - 5.23s]: First segment of speech
[5.23s - 10.45s]: Second segment of speech
[10.45s - 15.67s]: Third segment of speech
...
```

## Tips for Best Results

1. **Audio Quality**: Higher quality audio = better transcription
2. **Format**: MP3, WAV, M4A all work well
3. **Length**: No limit, but longer videos take more time
4. **Languages**: Whisper supports 99+ languages automatically

## Troubleshooting

If transcription fails:
1. Check audio file format and size
2. Ensure the file isn't corrupted
3. Try a smaller segment first
4. Check available disk space

## Next Steps

Once you have the audio file, simply run:
```bash
python transcribe_youtube.py --file /path/to/your/audio.mp3
```

The script will handle the rest automatically!