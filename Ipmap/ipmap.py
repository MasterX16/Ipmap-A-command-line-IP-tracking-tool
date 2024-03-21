#!/usr/bin/env python3
#This is the main ipmap file

# MIT License
#
# Copyright (c) 2024 MasterX16
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from ip2geotools.databases.noncommercial import DbIpCity
import argparse
from colorama import Fore,Style
import os 
from socket import gethostbyname,gaierror
from map_func import *
from Wordlist import wordlist_loc
from save_txt import txt
import json


class Ip:
    def __init__(self,ip,file,sep,ipli):
   
      self.ip = ip
      
        #print(f"{Fore.RED}{Style.BRIGHT}[-]{Fore.RESET}Invalid ip address:{self.ip}")
      self.sep = sep
      self.ipli = ipli
      self.wordlist = None
      if file is not None:
         if os.path.exists(file):
            with open (file,'r') as file:
                temp = file.read()
                self.wordlist = temp.split(sep)
         else:
            print("Invalid file path!")        
        

    def print_info(self):
        location = self.get_loc()
        
        self.region = location.region
        self.city = location.city
        self.latitude = location.latitude
        self.longtitude = location.longitude
        self.country = location.country


        print(f"{Fore.GREEN}{Style.BRIGHT}[+]Ip:{self.ip}")
        print("\n")
        print(f"{Fore.BLUE}{Style.BRIGHT}Location info on {self.ip}\n")
        print("-"*50)
        print(f"{Fore.GREEN}{Style.BRIGHT}Country:{Fore.RESET}{Fore.YELLOW}{self.country}")
        print(f"{Fore.GREEN}{Style.BRIGHT}Region:{Fore.RESET}{Fore.CYAN}{self.region}")
        print(f"{Fore.GREEN}{Style.BRIGHT}City:{Fore.RESET}{Fore.LIGHTYELLOW_EX}{self.city}")
        print(f"{Fore.GREEN}{Style.BRIGHT}Latitude:{Fore.RESET}{self.latitude}")
        print(f"{Fore.GREEN}{Style.BRIGHT}Longtitude:{Fore.RESET}{self.longtitude}")
    
    def map_self(self):
        map_ip(self.ip,self.latitude,self.longtitude)
        print("\n")
        print(f"{Fore.GREEN}[+]Map saved at {self.ip}.html")
    
    def get_loc(self):
        try:
          location = DbIpCity.get(gethostbyname(self.ip),api_key='free')
          return location
        except Exception as e:
             print(f"{Fore.RED}{Style.BRIGHT}[-]Error!{Fore.RESET}Invalid ip address/website provided:{ip}")
             exit()

    def wordlist_loc(self):
      if self.wordlist is not None:
       for ip in self.wordlist:
         self.ip = ip
         self.print_info()
         

    def wordlist_retlist(self):
        ip_data_list = []  # List to store geolocation information for each IP in the wordlist

        if self.wordlist is not None:
         for ip in self.wordlist:
            try:
                self.ip = gethostbyname(ip)
            except gaierror:
                print(f"{Fore.RED}{Style.BRIGHT}[-]{Fore.RESET}Invalid ip address:{ip}!")    
               
            location = self.get_loc()
            ip_data = {
                    'IP': ip,
                    'Country': location.country,
                    'Region': location.region,
                    'City': location.city,
                    'Latitude': location.latitude,
                    'Longitude': location.longitude
                }
            ip_data_list.append(ip_data)

        return ip_data_list     

    def wordlist_map(self):
       if self.wordlist is not None:
          for ip in self.wordlist:
             self.ip = ip
             self.map_self()     
    
    def m_map(self):
       latitudes = []
       longtitudes = []
       ips = []
       if self.wordlist is not None:
          for ip in self.wordlist:
             ips.append(ip)
             self.ip = ip
             location = self.get_loc()
             latitudes.append(location.latitude)
             longtitudes.append(location.longitude)
       elif self.ipli is not None:
          for ip in self.ipli:
             ips.append(gethostbyname(ip))
             location = self.get_loc()
             latitudes.append(location.latitude)
             longtitudes.append(location.longitude)      
             
       multi_map(ips,latitudes=latitudes,longtitudes=longtitudes)

    def save_json(self,filename):
     ip_data_list = None
     if ".json" in filename:
         filename = filename.replace(".json","")  

     if self.wordlist:
        ip_data_list = self.wordlist_retlist()
     elif self.ipli:
        for ip in self.ipli:
            self.ip = ip
            location = self.get_loc()
            ip_data = {
                'IP': ip,
                'Country': location.country,
                'Region': location.region,
                'City': location.city,
                'Latitude': location.latitude,
                'Longitude': location.longitude
            }
            ip_data_list.append(ip_data)
     else:  # Single IP case
        location = self.get_loc()
        ip_data = {
            'IP': self.ip,
            'Country': location.country,
            'Region': location.region,
            'City': location.city,
            'Latitude': location.latitude,
            'Longitude': location.longitude
        }
        ip_data_list.append(ip_data)
        
     with open(filename + ".json", 'w') as file:
         json.dump(ip_data_list, file, indent=4)

     print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Fore.RESET}{Style.RESET_ALL}Data of IPs saved successfully to {filename+'.json'}!")
 
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-ip","--ip",default=None,type=str,help="Specify the ip to locate.") 
group.add_argument("-w","--w",type=str,default=None,help="Give a wordlist of ips.")
group.add_argument("-ipli","--ipli",type=str,default=None,help="Give a list of ips directly.")
parser.add_argument("-sep","--sep",default=",",help="Iterates through the wordlist sepearated by this argument.")
parser.add_argument("-map","--map",default=False,required=False,help="Save the map of an ip toan html file",action="store_true")
parser.add_argument("-geo","--geo",default=False,required=False,help="Print the geolocation info of the Ip.",action="store_true")
parser.add_argument("-txt","--txt",type=str,default=None,required=False,help="Save the data to a txt file.",)
parser.add_argument("-json","--json",type=str,default=None,required=False,help="Save the data to a json file.")
args = parser.parse_args()
ip = None
if args.ip is not None:
   try:
     ip = gethostbyname(args.ip)
   except gaierror:
    print(f"{Fore.RED}{Style.BRIGHT}[-]{Fore.RESET}Invalid ip address:{ip}!")    
   
ip = Ip(ip,args.w,args.sep,args.ipli)

wordlist = False
is_ip = False
is_ipli = False
if args.w is not None:
   wordlist= True
      

if args.ip is not None:
   is_ip =True

if is_ipli is not None:
   is_ipli = True


if not args.geo and not args.map and args.txt is None and args.json is None:
    print(f"{Fore.RED}{Style.BRIGHT}[-]{Fore.RESET}No output method specified (-geo, -map, -txt, -json)!")
    exit(0)



if is_ip:
   if args.geo:
    ip.print_info()
   if args.map:
      ip.map_self()
   if args.txt is not None:
      txt(args.ip,args.txt,ip.get_loc())   
   if args.json is not None:
      ip.save_json(args.json)   

if wordlist:
   if args.geo:
    ip.wordlist_loc()
   if args.map:
      ip.m_map() 
   if args.txt is not None:
     
      with open(args.txt+'.txt', 'w') as txt_file:
            result = ip.wordlist_retlist()
            for ip_data in result:
                txt_file.write(f"Ip: {ip_data['IP']}\n")
                txt_file.write(f"Country: {ip_data['Country']}\n")
                txt_file.write(f"Region: {ip_data['Region']}\n")
                txt_file.write(f"City: {ip_data['City']}\n")
                txt_file.write(f"Latitude: {ip_data['Latitude']}\n")
                txt_file.write(f"Longitude: {ip_data['Longitude']}\n")    
                txt_file.write("\n")

      print(f"\n{Fore.GREEN}{Style.BRIGHT}[+]{Fore.RESET}Data succesfully saved to {args.txt+'.txt'}!") 
    
   if args.json is not None:
      ip.save_json(args.json)
      
      
   
if is_ipli and args.ipli is not None:
   ipli = args.ipli.split(',')
   if args.geo:
      for ip in ipli:
         ip_obj = Ip(ip,args.w,args.sep,args.ipli)
         ip_obj.print_info()
   if args.map:
      ip_tmp = Ip(args.ip,args.w,args.sep,ipli)
      ip_tmp.m_map()
   if args.json is not None:
      ip_tmp = Ip(args.ip,args.w,args.sep,ipli)
      ip_tmp.save_json(args.json)

