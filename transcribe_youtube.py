#!/usr/bin/env python3

import os
import sys
import subprocess
import whisper
from pathlib import Path
import argparse

def download_audio_with_cookies(youtube_url, output_dir="./downloads"):
    """Download audio from YouTube video using cookies from browser"""
    print(f"Downloading audio from: {youtube_url}")
    
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(exist_ok=True)
    
    # Try downloading with cookies from browser
    audio_file = os.path.join(output_dir, "audio.%(ext)s")
    
    # First try with cookies from Firefox
    cmd = [
        "yt-dlp",
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "--cookies-from-browser", "firefox",
        "-o", audio_file,
        youtube_url
    ]
    
    try:
        print("Trying to download with Firefox cookies...")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("Audio downloaded successfully with Firefox cookies!")
        
        # Find the actual downloaded file
        for file in Path(output_dir).glob("audio.*"):
            return str(file)
            
    except subprocess.CalledProcessError:
        print("Firefox cookies method failed, trying Chrome...")
        
        # Try with Chrome cookies
        cmd[5] = "chrome"
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print("Audio downloaded successfully with Chrome cookies!")
            
            # Find the actual downloaded file
            for file in Path(output_dir).glob("audio.*"):
                return str(file)
                
        except subprocess.CalledProcessError:
            print("Chrome cookies method also failed.")
            return None

def download_audio_simple(youtube_url, output_dir="./downloads"):
    """Try simple download without authentication"""
    print(f"Downloading audio from: {youtube_url}")
    
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(exist_ok=True)
    
    audio_file = os.path.join(output_dir, "audio.%(ext)s")
    
    # Try multiple methods
    methods = [
        # Method 1: Basic download
        [
            "yt-dlp",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            "-o", audio_file,
            youtube_url
        ],
        # Method 2: With user agent
        [
            "yt-dlp",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "-o", audio_file,
            youtube_url
        ],
        # Method 3: Different format selection
        [
            "yt-dlp",
            "--format", "bestaudio[ext=m4a]",
            "--extract-audio",
            "--audio-format", "mp3",
            "-o", audio_file,
            youtube_url
        ]
    ]
    
    for i, cmd in enumerate(methods, 1):
        try:
            print(f"Trying download method {i}...")
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"Audio downloaded successfully with method {i}!")
            
            # Find the actual downloaded file
            for file in Path(output_dir).glob("audio.*"):
                return str(file)
                
        except subprocess.CalledProcessError as e:
            print(f"Method {i} failed: {e.stderr.split('\n')[-2] if e.stderr else 'Unknown error'}")
            continue
    
    return None

def transcribe_audio(audio_file, model_name="base"):
    """Transcribe audio using OpenAI Whisper"""
    print(f"Loading Whisper model: {model_name}")
    model = whisper.load_model(model_name)
    
    print(f"Transcribing: {audio_file}")
    result = model.transcribe(audio_file)
    
    return result

def save_transcript(result, output_file="transcript.txt"):
    """Save transcript to file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("FULL TRANSCRIPT:\n")
        f.write("=" * 50 + "\n\n")
        f.write(result["text"].strip())
        f.write("\n\n" + "=" * 50 + "\n")
        f.write("SEGMENTS WITH TIMESTAMPS:\n")
        f.write("=" * 50 + "\n\n")
        
        for segment in result["segments"]:
            start_time = segment["start"]
            end_time = segment["end"]
            text = segment["text"].strip()
            f.write(f"[{start_time:.2f}s - {end_time:.2f}s]: {text}\n")
    
    print(f"Transcript saved to: {output_file}")

def transcribe_local_file(file_path):
    """Transcribe a local audio file"""
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        return 1
        
    print(f"Transcribing local file: {file_path}")
    
    try:
        result = transcribe_audio(file_path, model_name="base")
        
        # Display transcript
        print("\n" + "=" * 50)
        print("TRANSCRIPT:")
        print("=" * 50)
        print(result["text"].strip())
        print("=" * 50)
        
        # Save to file
        save_transcript(result, f"transcript_{Path(file_path).stem}.txt")
        
        print("\nTranscription completed successfully!")
        return 0
        
    except Exception as e:
        print(f"Error during transcription: {e}")
        return 1

def main():
    parser = argparse.ArgumentParser(description="Transcribe YouTube videos or local audio files")
    parser.add_argument("--file", "-f", help="Local audio file to transcribe")
    parser.add_argument("--url", "-u", help="YouTube URL to download and transcribe")
    parser.add_argument("--model", "-m", default="base", help="Whisper model to use (tiny, base, small, medium, large)")
    
    args = parser.parse_args()
    
    print("YouTube Video/Audio Transcription Tool")
    print("=" * 40)
    
    # If local file is provided, transcribe it directly
    if args.file:
        return transcribe_local_file(args.file)
    
    # Use provided URL or default
    youtube_url = args.url or "https://youtu.be/Yjll-IOhHPY?si=5JShdY_bO91mdiqP"
    
    print("IMPORTANT: Due to YouTube's bot protection, downloading may fail.")
    print("If download fails, you can:")
    print("1. Download the video manually using a browser")
    print("2. Extract audio and save it as 'audio.mp3' in ./downloads/")
    print("3. Run: python transcribe_youtube.py --file ./downloads/audio.mp3")
    print("=" * 40)
    
    # Try downloading with cookies first
    audio_file = download_audio_with_cookies(youtube_url)
    
    # If that fails, try simple download
    if not audio_file:
        audio_file = download_audio_simple(youtube_url)
    
    if not audio_file:
        print("\nDownload failed. Manual instructions:")
        print("1. Go to: " + youtube_url)
        print("2. Download the video using a browser extension or online converter")
        print("3. Convert to MP3 and save as './downloads/audio.mp3'")
        print("4. Run: python transcribe_youtube.py --file ./downloads/audio.mp3")
        
        # Check if there's already a file in downloads
        downloads_dir = Path("./downloads")
        if downloads_dir.exists():
            audio_files = list(downloads_dir.glob("*.mp3")) + list(downloads_dir.glob("*.wav")) + list(downloads_dir.glob("*.m4a"))
            if audio_files:
                print(f"\nFound existing audio file: {audio_files[0]}")
                choice = input("Would you like to transcribe this file? (y/n): ").strip().lower()
                if choice == 'y':
                    return transcribe_local_file(str(audio_files[0]))
        
        return 1
    
    print(f"Audio file: {audio_file}")
    
    # Transcribe audio
    try:
        result = transcribe_audio(audio_file, model_name=args.model)
        
        # Display transcript
        print("\n" + "=" * 50)
        print("TRANSCRIPT:")
        print("=" * 50)
        print(result["text"].strip())
        print("=" * 50)
        
        # Save to file
        save_transcript(result)
        
        # Clean up audio file
        try:
            os.remove(audio_file)
            print(f"Cleaned up temporary audio file: {audio_file}")
        except:
            pass
            
        print("\nTranscription completed successfully!")
        return 0
        
    except Exception as e:
        print(f"Error during transcription: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())