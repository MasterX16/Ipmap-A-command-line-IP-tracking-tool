#File for map functions
#Author:MaterX16
# MIT License
#
# Copyright (c) 2024 MasterX
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

from folium import Map,Marker
from colorama import Fore,Style

def map_ip(ip,latitude,longtitude):
    ip_map = Map(location=[latitude,longtitude],zoom_start=12)
    marker = Marker(location=[latitude,longtitude],popup=ip)
    marker.add_to(ip_map)
    ip_map.save(f"{ip}.html")


def multi_map(ips,latitudes,longtitudes):
    ip_map = Map(location=[latitudes[0],longtitudes[0]],zoom_start=12)
    for ip,latitude,longtitude in zip(ips,latitudes,longtitudes):
        marker = Marker(location=[latitude,longtitude],popup=ip)
        marker.add_to(ip_map)
    name = str(input("Enter the name of the map to save all marked ips:"))
    ip_map.save(name+".html")
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Fore.RESET}Map saved succesfully to "+name+".html,you can view it in your browser!")
    