#!/usr/bin/env python3
"""
Quick audio generator - just paste your text!
Usage: python3 quick_speak.py "Your English text here"
"""

import asyncio
import edge_tts
import sys
import os
import subprocess
from datetime import datetime

async def generate_and_play(text: str, voice: str = "en-US-AndrewNeural", rate: str = "+0%"):
    """Generate and play audio"""
    # Create output directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    audio_dir = os.path.join(script_dir, "audio")
    os.makedirs(audio_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(audio_dir, f"speech_{timestamp}.mp3")
    
    print(f"Generating audio...")
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(output_file)
    
    print(f"Saved: {output_file}")
    print(f"Playing... Listen and shadow read!")
    print("-" * 50)
    print(f"Text: {text}")
    print("-" * 50)
    
    # Play audio
    subprocess.run(["afplay", output_file], check=True)
    print("Done! Your turn to practice!")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 quick_speak.py \"Your English text here\"")
        print("\nExamples:")
        print('  python3 quick_speak.py "Hello, welcome to my presentation."')
        print('  python3 quick_speak.py "Today I would like to talk about..."')
        sys.exit(1)
    
    text = " ".join(sys.argv[1:])
    asyncio.run(generate_and_play(text))

if __name__ == "__main__":
    main()
