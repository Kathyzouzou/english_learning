#!/usr/bin/env python3
"""
Generate remaining audio files
"""

import asyncio
import edge_tts
import os

# Remaining speech parts (from 05a onwards)
SPEECH_PARTS = [
    ("05a_more_examples", 
     "Besides websites, what else can Vibe Coding do? Let me show you a few more interesting examples — all built this way."),
    
    ("05b_booth", 
     "First: a booth simulator. If you're thinking about setting up a booth, you can try out what your future booth might look like."),
    
    ("05c_travel", 
     "Second: a travel planning tool. It generates a complete trip plan — where to go each day, what to do and when. The best part? It connects directly to Google Maps — one tap and you're navigating. There's also an expense tracker for splitting costs after the trip."),
    
    ("05d_nutrition", 
     "Third: a nutrition label scanner. Ever picked up a snack at the supermarket, looked at all those chemical names on the back, and had no idea if it's healthy? This tool solves that. Take a photo of the package, and AI analyzes the ingredients, telling you in plain language what you're really eating."),
    
    ("05e_stock", 
     "Fourth: a stock trading assistant. This one's a bit hardcore. It automatically scrapes stock data, has AI analyze charts, identify key patterns, and generates a daily report — helping avoid emotional trading."),
    
    ("05f_more_tools", 
     "The fifth example is a Figma plugin I made, and the sixth is a shadow reading practice tool — I'll share those at the end."),
    
    ("05g_common_point", 
     "You'll notice these examples have something in common: they all solve a specific problem for a specific person. Before, if you had a small pain point, you'd probably just live with it — building a dedicated tool felt like too much work. Now it's different. You have an idea, describe it clearly, and in a few hours — sometimes even minutes — you have something that works. That's what excites me most about Vibe Coding — it lets ordinary people turn ideas into products."),
    
    ("06a_limitations", 
     "Of course, there are things it can't do. For complex systems, scenarios that require strict design systems, or products like finance and payments where stability is critical — handwritten code with rigorous testing is still more reliable."),
    
    ("06b_summary", 
     "So here's how I see it: Vibe Coding is great for the zero-to-one phase, for quickly validating ideas."),
    
    ("07a_meta", 
     "One last thing I find quite interesting. The website you're looking at right now — it's about Vibe Coding, and it was itself built with Vibe Coding. I barely wrote any code. I just kept describing what I wanted to the AI. From idea to launch, about 45 minutes, around 14 rounds of conversation. So if you ask me whether Vibe Coding actually works, my answer is: you're looking at the proof."),
    
    ("07b_closing", 
     "That's all from me today. Yuyuan will show you how the tools actually work in a moment. If you're curious, I encourage you to try it yourself. Thank you."),
    
    ("08a_figma_problem", 
     "When we deliver designs in Figma, we need to find the cover template file first, then choose the type, write the title, translate the title, take a screenshot, set it as cover — and we often can't find our own design files."),
    
    ("08b_figma_plugin", 
     "So I used Vibe Coding to build a plugin called \"Quick Cover Generator.\" You can pick the project type — Trip, Ctrip, C&T, Collection, To B, whatever you want. Then add tags, fill in the title, and one click translates the Chinese title to English automatically. You can also capture your current page as a thumbnail with one click. The best part — you can put your own avatar on the cover. That way, in a sea of files, you can instantly spot which ones are yours."),
    
    ("08c_figma_time", 
     "The whole plugin, from idea to working product, took about an afternoon. If you think Figma is missing some plugin, or there's some repetitive work you'd like to automate, try building one yourself."),
    
    ("09_shadow_reading", 
     "Finally, to practice for this English presentation, I built a shadow reading practice tool. Let me show you how it works."),
]

async def generate_all():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    audio_dir = os.path.join(script_dir, "speech_audio")
    os.makedirs(audio_dir, exist_ok=True)
    
    voice = "en-US-AndrewNeural"
    rate = "-5%"
    
    print(f"Generating {len(SPEECH_PARTS)} remaining audio files...")
    print("-" * 60)
    
    for i, (filename, text) in enumerate(SPEECH_PARTS, 1):
        output_file = os.path.join(audio_dir, f"{filename}.mp3")
        print(f"[{i}/{len(SPEECH_PARTS)}] Generating {filename}.mp3...")
        
        communicate = edge_tts.Communicate(text, voice, rate=rate)
        await communicate.save(output_file)
        print(f"    Done!")
    
    print("-" * 60)
    print(f"Done! All files saved.")

if __name__ == "__main__":
    asyncio.run(generate_all())
