# BASIC CTFLERDE XOR DECOD ETMEK İÇİN GELİŞTİRİLDİ
# HAPPY HACKING!!

import os
import time
import sys
from colorama import init, Fore, Back, Style

init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(text, duration=1.5):
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for i in range(int(duration * 10)):
        sys.stdout.write(f'\r{Fore.YELLOW}{chars[i % len(chars)]} {text}...')
        sys.stdout.flush()
        time.sleep(0.1)
    print(f'\r{Fore.GREEN}✓ {text} tamamlandı!{Style.RESET_ALL}')

def xor_encrypt(text):
    keys = ['T', 'H', 'M', '{', '}']
    output = []
    for i in range(4):
        output.append(chr(ord(text[i]) ^ ord(keys[i])))
    output.append(chr(ord(text[-1]) ^ ord(keys[4])))
    return "".join(output)

def main():
    clear_screen()
    
    hex_string = input(f"{Fore.GREEN}📥 Hex string: {Style.RESET_ALL}").strip()
    
    loading_animation("Hex decode")
    xored_original = bytes.fromhex(hex_string).decode('utf-8')
    
    print(f"\n{Fore.MAGENTA}🔍 XOR data: {Style.RESET_ALL}{xored_original}")
    
    loading_animation("Key generate")
    key = xor_encrypt(xored_original)
    
    print(f"{Fore.CYAN}🔑 Key: {Style.RESET_ALL}{key}")
    
    loading_animation("Flag decrypt")
    flag = ""
    for i in range(len(xored_original)):
        flag += chr(ord(xored_original[i]) ^ ord(key[i % len(key)]))
    
    print(f"\n{Fore.RED}{'='*40}")
    print(f"{Fore.YELLOW}🎉 FLAG: {flag}{Style.RESET_ALL}")
    print(f"{Fore.RED}{'='*40}{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except:
        pass
