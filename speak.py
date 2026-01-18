#!/usr/bin/env python3
"""
English Shadow Reading Practice Tool
Generate native English audio for shadow reading practice
"""

import asyncio
import edge_tts
import sys
import os
import subprocess
from datetime import datetime

# Available voices for practice
VOICES = {
    "1": ("en-US-AndrewNeural", "Andrew (Male, American) - Warm, Confident"),
    "2": ("en-US-AvaNeural", "Ava (Female, American) - Expressive, Friendly"),
    "3": ("en-US-JennyNeural", "Jenny (Female, American) - Friendly, Natural"),
    "4": ("en-GB-RyanNeural", "Ryan (Male, British) - Professional"),
    "5": ("en-GB-SoniaNeural", "Sonia (Female, British) - Clear, Professional"),
}

# Default voice
DEFAULT_VOICE = "en-US-AndrewNeural"

async def generate_audio(text: str, voice: str, output_file: str, rate: str = "+0%"):
    """Generate audio from text using edge-tts"""
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(output_file)
    return output_file

def play_audio(file_path: str):
    """Play audio file using macOS afplay"""
    subprocess.run(["afplay", file_path], check=True)

def main():
    print("\n" + "="*60)
    print("  English Shadow Reading Practice Tool")
    print("="*60)
    
    # Show available voices
    print("\nAvailable voices:")
    for key, (voice_id, desc) in VOICES.items():
        print(f"  {key}. {desc}")
    
    # Select voice
    voice_choice = input("\nSelect voice (1-5, default=1): ").strip() or "1"
    voice = VOICES.get(voice_choice, VOICES["1"])[0]
    print(f"Using: {VOICES.get(voice_choice, VOICES['1'])[1]}")
    
    # Select speed
    print("\nSpeed options:")
    print("  1. Slow (-20%) - Good for beginners")
    print("  2. Normal (0%) - Natural speed")
    print("  3. Fast (+15%) - Challenge mode")
    
    speed_choice = input("Select speed (1-3, default=2): ").strip() or "2"
    speed_map = {"1": "-20%", "2": "+0%", "3": "+15%"}
    rate = speed_map.get(speed_choice, "+0%")
    
    print("\n" + "-"*60)
    print("Enter your English text (or 'quit' to exit):")
    print("-"*60)
    
    # Create output directory
    output_dir = os.path.dirname(os.path.abspath(__file__))
    audio_dir = os.path.join(output_dir, "audio")
    os.makedirs(audio_dir, exist_ok=True)
    
    counter = 1
    while True:
        print()
        text = input(">> ").strip()
        
        if text.lower() in ['quit', 'exit', 'q']:
            print("\nGood luck with your speech! You've got this!")
            break
        
        if not text:
            continue
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%H%M%S")
        output_file = os.path.join(audio_dir, f"practice_{counter:03d}_{timestamp}.mp3")
        
        print(f"  Generating audio...")
        try:
            asyncio.run(generate_audio(text, voice, output_file, rate))
            print(f"  Saved: {output_file}")
            print(f"  Playing audio... (Listen and repeat!)")
            play_audio(output_file)
            print(f"  Done! Now it's your turn to practice.")
            counter += 1
        except Exception as e:
            print(f"  Error: {e}")

if __name__ == "__main__":
    main()
