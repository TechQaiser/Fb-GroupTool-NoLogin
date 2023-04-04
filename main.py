from requests import get
import codecs, sys, os
from time import sleep
from re import findall,search
from random import choice
from os import system as stm
# --->>> colors
red='\033[1;91m'
green='\033[1;92m'
yellow='\033[1;93m'
blue='\033[1;94m'
pink='\033[1;95m'
cyan='\033[1;96m'
lred='\033[1;31m'
lgreen='\033[1;32m'
lyellow='\033[1;33m'
lblue='\033[1;34m'
lpink='\033[1;35m'
lcyan='\033[1;36m'
stop='\033[0m'
color = ["\033[0;32m", "\033[1;32m","\033[0;92m","\033[1;92m","\033[1;93m","\033[1;95m","\033[1;96m","\033[0;33m", "\033[1;33m", "\033[1;34m", "\033[0;35m", "\033[1;35m", "\033[0;36m", "\033[1;36m"]
random_color = choice(color)
random_color2 = choice(color)

def slow_writter(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.05)

# --->>> logo
logo = f"""
{random_color2}{95*'-'}{stop}
	{random_color}
    
 .d88888b.   .d8888b.  8888888b.        8888888888 888888b.           .d8888b.  8888888b.  8888888b.  
d88P" "Y88b d88P  Y88b 888   Y88b       888        888  "88b         d88P  Y88b 888   Y88b 888   Y88b 
888     888 Y88b.      888    888       888        888  .88P         888    888 888    888 888    888 
888     888  "Y888b.   888   d88P       8888888    8888888K.         888        888   d88P 888   d88P 
888     888     "Y88b. 8888888P"        888        888  "Y88b        888  88888 8888888P"  8888888P"  
888 Y8b 888       "888 888 T88b  888888 888        888    888 888888 888    888 888 T88b   888        
Y88b.Y8b88P Y88b  d88P 888  T88b        888        888   d88P        Y88b  d88P 888  T88b  888        
 "Y888888"   "Y8888P"  888   T88b       888        8888888P"          "Y8888P88 888   T88b 888        
       Y8b                                                                                            {stop}
{random_color2}{95*'-'}{stop}
        {random_color}  -> Tool Is Developed by : Qsr
          -> Youtube Channel Name : Tech Qsr
          -> Contact : Github -->> @TechQaiser{stop} 
{random_color2}{95*'-'}{stop}"""

def file_creater():
    slow_writter(f'nstalling Tool In Your Device Wait Creating Files Of Data ')
    sleep(2)
    os.mkdir('Data')
    slow_writter(f' Created Folder SucessFully  /Data SucessFully')
    sleep(2)
    open('Data/minimum_admins.txt','a')
    slow_writter(f'  File Data/minimum_admins.txt Created SucessFully')
    sleep(2)
    open('Data/total_members.txt', 'a')
    slow_writter(f'  File Data/total_members.txt Created SucessFully')
    sleep(2)
    open('Data/all_data_mix.txt', 'a')
    slow_writter(f' File Data/all_data_mix.txt Created SucessFully')
    sleep(2)
    open('Data/posts_per_days.txt ', 'a')
    slow_writter(f'  File Data/posts_per_days.txt Created SucessFully')
    slow_writter(f' All Files Are Created SucessFully ')
    sleep(1.2)
    print(f" -> Redirecting To Main Page ..... ")
    sleep(2)
if not os.path.exists('Data'):
    file_creater()

def main_dashboard():
    stm('cls');print(logo)
    print(" 1. Check Group (Admin,Members,Posts) Mix")
    print(" 2. Check Group Per Day/month Posts")
    print(" 3. Check Groups Total Admins")
    print(" 4. Check Group Total Members")
    print(" 0. Exit Tool Go Back")
    print(95 * f'{random_color2}-{stop}')
    parser = input(' Select Option TO Use -> ')
    if parser in ['1','01']:
        main().MIX_checker()
    if parser in ['2','02']:
        main().day_posts()
    if parser in ['3','03']:
        main().total_admins()
    if parser in ['4','04']:
        main().total_members()
    if parser in ['0','00']:
        pass

class main():
    def __init__(self):
        stm('cls');print(logo)
        self.file = open('data.txt', 'r').readlines()
        self.head: dict = {
            'Host': 'web.facebook.com',
            'Sec-Ch-Ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.111 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'close'
        }
    def re_data(self, po, data='both'):
        admins = findall('admin_profiles":{"count":(.*?),', str(po))[0]
        total_members = search(r'"group_total_members_info_text":"\s*([\d,]+)\s*', str(po)).group(1)
        posts_per_day = search(r'number_of_posts_in_last_day":(.*?),', str(po)).group(1)
        posts_in_month = search(r'number_of_posts_in_last_month":(.*?),', str(po)).group(1)
        group_name = search(r':"Group","name":"(.*?)",', str(po)).group(1)
        if data == "admins":
            return admins
        elif data == "total_members":
            return total_members
        elif data == "posts_per_day":
            return posts_per_day
        elif data == "posts_in_month":
            return posts_in_month
        elif data == "group_name":
            return group_name
        elif data == "all":
            return admins, total_members, posts_per_day, posts_in_month, group_name
    def data_sender(self,group_ids):
        po = get(f'https://web.facebook.com/groups/{group_ids}/about', headers=self.head).text
        return po
    def MIX_checker(self):
        for group_ids in self.file:
            group_ids = group_ids.replace('\n', '')
            po = self.data_sender(group_ids)
            int(group_ids.strip())
            try:
                admins = self.re_data(po, 'admins')
                total_members = self.re_data(po,'total_members')
                posts_per_day = self.re_data(po,'posts_per_day')
                posts_in_month = self.re_data(po,'posts_in_month')
                group_name = self.re_data(po,'group_name')
                try:
                    group_name = codecs.encode(group_name.encode('utf-8').decode('unicode-escape'), 'utf-16','surrogatepass').decode('utf-16')
                except (ValueError, UnicodeEncodeError):
                    pass
                print(f'{pink}-> GROUP NAME {lpink}:{pink} {group_name} {stop}')
                print(f"    {cyan}-->>{stop} Group [{group_ids}] {lcyan}•{stop} {lgreen}Admins{stop} [{admins}] {lcyan}•{stop} {yellow}total members{stop} [{total_members}]")
                print(f'        {cyan}-->>{stop} {lblue}Posts per day{stop} [{posts_per_day}] {lcyan}•{stop} {lred}Posts in month{stop} : {posts_in_month}')
                open('Data/all_data_mix.txt', 'a', encoding='utf-8').write(group_ids+'|'+group_name+'|'+'admins:'+admins+'|'+'members:'+total_members+'|'+'posts_day:'+posts_per_day+'\n')
            except IndexError:
                print(' something went wrong with this group {}'.format(group_ids))
        exit(' process completed')
    def day_posts(self):
        minimum_posts_per_day = open('minimum_posts_day.txt','r').readline()
        for group_ids in self.file:
            group_ids = group_ids.replace('\n', '')
            po = self.data_sender(group_ids)
            int(group_ids.strip())
            try:
                posts_per_day = self.re_data(po, 'posts_per_day')
                posts_in_month = self.re_data(po, 'posts_in_month')
                group_name = self.re_data(po, 'group_name')
                try:
                    group_name = codecs.encode(group_name.encode('utf-8').decode('unicode-escape'), 'utf-16','surrogatepass').decode('utf-16')
                except (ValueError, UnicodeEncodeError):
                    pass
                print(f'{pink}->  Group [{group_ids}] {lpink}:{pink} {group_name} {stop}')
                print(f'    {cyan}-->>{stop} {lblue}Posts per day{stop} [{posts_per_day}] {lcyan}•{stop} {lred}Posts in month{stop} : {posts_in_month}')
                if int(posts_per_day) > int(minimum_posts_per_day):
                    with open('Data/posts_per_days.txt', 'a', encoding='utf-8') as f:
                        f.write(f"{group_ids}|{posts_per_day}\n")
            except IndexError:
                print(' something went wrong with this group {}'.format(group_ids))
        exit(' process completed')
    def total_admins(self):
        minimum_admins = open('minimum_admins.txt','r').readline()
        for group_ids in self.file:
            group_ids = group_ids.replace('\n', '')
            po = self.data_sender(group_ids)
            int(group_ids.strip())
            try:
                admins = self.re_data(po, 'admins')
                total_members = self.re_data(po,'total_members')
                group_name = self.re_data(po,'group_name')
                try:
                    group_name = codecs.encode(group_name.encode('utf-8').decode('unicode-escape'), 'utf-16','surrogatepass').decode('utf-16')
                except (ValueError, UnicodeEncodeError):
                    pass
                print(f'{pink}-> Group [{group_ids}] {lpink}:{pink} {group_name} {stop}')
                print(f"    {cyan}-->>{stop} {lgreen}Admins{stop} [{admins}] {lcyan}•{stop} {yellow}total members{stop} [{total_members}]")
                if int(admins) == int(minimum_admins):
                    with open('Data/minimum_admins.txt', 'a', encoding='utf-8') as f:
                        f.write(f"{group_ids}|members:{total_members}\n")
            except IndexError:
                print(' something went wrong with this group {}'.format(group_ids))
        exit(' process completed')
    def total_members(self):
        minimum_members = open('minimum_members.txt','r').readline()
        for group_ids in self.file:
            group_ids = group_ids.replace('\n', '')
            po = self.data_sender(group_ids)
            int(group_ids.strip())
            try:
                total_members = self.re_data(po,'total_members')
                print(f'{pink}-> {stop} Group [{group_ids}] {lpink}:{pink} {total_members} {stop}')
                if int(total_members.replace(',','')) > int(minimum_members):
                    with open('Data/total_members.txt', 'a', encoding='utf-8') as f:
                        f.write(f"{group_ids}|{total_members}\n")
            except IndexError:
                print(' something went wrong with this group {}'.format(group_ids))
        exit(' process completed')

if __name__ == '__main__':
    main_dashboard()