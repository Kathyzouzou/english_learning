#!/usr/bin/env python3
"""
Generate audio for the Vibe Coding speech - Updated Version
"""

import asyncio
import edge_tts
import os

# Updated speech parts
SPEECH_PARTS = [
    ("00_intro", 
     "Hi everyone, I'm Zexuan. Today I want to share something I've been really excited about lately. First, please open this website — you can switch between Chinese and English in the top right corner. I built this page a little while ago. Let me ask you: how long do you think it took me to make this? Some of you might guess a day or two, maybe a week? Actually, from scratch to launch, about 45 minutes. And I didn't write a single line of CSS. That's not because I suddenly learned to code. It's because I used a new approach called Vibe Coding."),
    
    ("01a_what_is_vibe", 
     "So what exactly is Vibe Coding? Simply put: I describe the product I want, and AI writes the code for me."),
    
    ("01b_old_way", 
     "The way we used to work — we'd create detailed mockups, mark every spacing, font size, and color, then hand it off to developers. We all know this process, and we all know how painful it can be. Want to change a small detail? Wait for the schedule, wait for development, wait for launch."),
    
    ("01c_new_way", 
     "Now it's different. I can just tell the AI: I think the information hierarchy isn't clear enough, or the layout doesn't look good, or even the product doesn't feel warm enough. As long as I describe my feelings, AI understands and updates the code directly. That's what Vibe means — I'm sharing feelings, not parameters."),
    
    ("02a_five_steps_intro", 
     "How do I actually use it? It's pretty simple. Five steps."),
    
    ("02b_five_steps_detail", 
     "Step one, have an idea — it can be vague, that's fine. Step two, describe it in plain language, no technical terms needed, just like chatting with a colleague. Step three, AI generates an MVP in seconds. Step four, see what's not right and keep talking — like \"make this button stand out more\" or \"this animation is too fast.\" Step five, when it feels ready, just launch it."),
    
    ("02c_key_point", 
     "What's the key point here? It's not about getting it perfect the first time. It's about fast iteration. Before, I'd hesitate to try uncertain ideas — what if it looks bad? Wouldn't that be a waste of effort? Now I don't overthink it. Trying something takes just seconds. If it doesn't work, I just try a different direction."),
    
    ("03a_demo_intro", 
     "Let me show you a demo."),
    
    ("03b_demo_animation", 
     "Look at this interactive demo. Same shape, but I describe its \"feeling\" with different words, and the animation is completely different. I say \"sharp,\" the animation becomes crisp and snappy. I say \"fluid,\" it becomes soft and elastic. I say \"bouncy,\" it springs back. I say \"heavy,\" it moves slowly, like it has weight. I didn't write any animation code. I just described the physical feeling I wanted."),
    
    ("04a_coffee_intro", 
     "Let me show you a more complete example. This is a coffee menu. I described it three different ways and got completely different results."),
    
    ("04b_coffee_v1", 
     "First version, I just said \"make me a coffee menu.\" What came out was a basic list — names, prices, functional but plain."),
    
    ("04c_coffee_v2", 
     "Second version, I said \"I want it to feel like a specialty coffee shop.\" Look — the layout became refined, the typography has layers, the whole style feels more professional."),
    
    ("04d_coffee_v3", 
     "Third version, I said \"late night, quiet, I want a pure sense of calm.\" This one is completely different — there's rain in the background, you can hear the rain, the whole mood shifted. We can even control how heavy the rain is."),
    
    ("04e_coffee_summary", 
     "Same content, different words, completely different results. That's what makes Vibe Coding fun — you're not tweaking parameters, you're shaping feelings."),
    
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
    
    # Clear old files
    for f in os.listdir(audio_dir):
        if f.endswith('.mp3'):
            os.remove(os.path.join(audio_dir, f))
    
    voice = "en-US-AndrewNeural"  # Professional male voice
    rate = "-5%"  # Slightly slower for practice
    
    print(f"Generating {len(SPEECH_PARTS)} audio files...")
    print(f"Voice: {voice}")
    print(f"Output directory: {audio_dir}")
    print("-" * 60)
    
    for i, (filename, text) in enumerate(SPEECH_PARTS, 1):
        output_file = os.path.join(audio_dir, f"{filename}.mp3")
        print(f"[{i}/{len(SPEECH_PARTS)}] Generating {filename}.mp3...")
        
        communicate = edge_tts.Communicate(text, voice, rate=rate)
        await communicate.save(output_file)
    
    print("-" * 60)
    print(f"Done! All {len(SPEECH_PARTS)} audio files saved to: {audio_dir}")

if __name__ == "__main__":
    asyncio.run(generate_all())
