#!/usr/bin/env python3
"""
Shadow Reading Practice Player
Play speech audio segments for practice
"""

import os
import subprocess
import sys

PARTS = [
    ("01_intro", "开场介绍 - Hi everyone, I'm [Your Name]..."),
    ("02_what_is_vibe", "什么是 Vibe Coding"),
    ("03_old_way", "传统工作方式"),
    ("04_new_way", "新的工作方式 - 传达感受而非参数"),
    ("05_five_steps", "五个步骤"),
    ("06_key_insight", "关键洞察 - 迭代成本低"),
    ("07_three_shifts", "三个转变（过渡句）"),
    ("08_shift1", "转变1 - 想法即时验证"),
    ("09_shift2", "转变2 - 设计不止于 Figma"),
    ("10_shift3", "转变3 - 敢于尝试不确定的想法"),
    ("11_demo_intro", "演示引入"),
    ("12_demo_animation", "动画演示 - sharp/fluid/bouncy/heavy"),
    ("13_coffee_intro", "咖啡菜单案例引入"),
    ("14_coffee_v1", "咖啡菜单 V1"),
    ("15_coffee_v2", "咖啡菜单 V2 - 精品店感觉"),
    ("16_coffee_v3", "咖啡菜单 V3 - 深夜宁静"),
    ("17_more_examples", "更多例子引入"),
    ("18_booth", "例子1 - 摊位模拟器"),
    ("19_travel", "例子2 - 旅游规划工具"),
    ("20_nutrition", "例子3 - 营养标签识别"),
    ("21_stock", "例子4 - 量化炒股助手"),
    ("22_figma", "例子5 - Figma 插件背景"),
    ("23_figma_plugin", "Figma 插件功能"),
    ("24_figma_time", "Figma 插件开发时间"),
    ("25_offer", "提供帮助"),
    ("26_common_point", "共同点 - 解决具体问题"),
    ("27_limitations", "局限性"),
    ("28_summary", "总结观点"),
    ("29_meta", "有趣的事 - 元叙事"),
    ("30_closing", "结尾"),
]

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    audio_dir = os.path.join(script_dir, "speech_audio")
    
    print("\n" + "="*60)
    print("  Vibe Coding 演讲 - 影子跟读练习")
    print("="*60)
    print("\n选择段落进行练习：\n")
    
    for i, (filename, desc) in enumerate(PARTS, 1):
        print(f"  {i:2d}. {desc}")
    
    print(f"\n  0. 全部播放")
    print(f"  q. 退出")
    
    while True:
        print()
        choice = input("请选择 (1-30, 0=全部, q=退出): ").strip().lower()
        
        if choice == 'q':
            print("\nGood luck with your speech! 加油！")
            break
        
        if choice == '0':
            print("\n开始全部播放...")
            for i, (filename, desc) in enumerate(PARTS, 1):
                filepath = os.path.join(audio_dir, f"{filename}.mp3")
                print(f"\n[{i}/30] {desc}")
                print("-" * 50)
                subprocess.run(["afplay", filepath])
                
                cont = input("按 Enter 继续，输入 q 退出: ").strip().lower()
                if cont == 'q':
                    break
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(PARTS):
                    filename, desc = PARTS[idx]
                    filepath = os.path.join(audio_dir, f"{filename}.mp3")
                    
                    print(f"\n播放: {desc}")
                    print("-" * 50)
                    subprocess.run(["afplay", filepath])
                    
                    replay = input("按 Enter 重播，输入其他数字切换段落: ").strip()
                    if replay == '':
                        subprocess.run(["afplay", filepath])
                else:
                    print("无效选择，请输入 1-30")
            except ValueError:
                print("无效输入")

if __name__ == "__main__":
    main()
