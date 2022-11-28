import os

# System call
os.system("")


# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

banner = style.GREEN + f"""
 =====================================================================
||  _____               _         _ _____                            ||
|| |_   _|___ ___ _____|_|___ ___| | __  |___ ___ _ _ _ ___ ___ ___  ||
||   | | | -_|  _|     | |   | .'| | __ -|  _| . | | | |_ -| -_|  _| ||
||   |_| |___|_| |_|_|_|_|_|_|__,|_|_____|_| |___|_____|___|___|_|   ||
||                                                                   ||
||                      {style.WHITE}          By: Baboucarr Badjie               {style.GREEN}||   
||{style.RED}                                    Please note this tool uses     {style.GREEN}||    
||{style.RED}                                webscraping tools to fetch data.   {style.GREEN}||       
||{style.RED}                                By using this tool, you agree      {style.GREEN}||   
||{style.RED}                                that you are responsible for any   {style.GREEN}||     
||{style.RED}                                violation of rules caused by this  {style.GREEN}||         
||{style.RED}                                tool!                              {style.GREEN}||    
 =====================================================================                                                                 
{style.RESET}"""
