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

from colorama import Fore,Style

def txt(ip,filename,location):
    if ".txt" in filename:
        filename = filename.replace(".txt","")
    region = location.region
    city = location.city
    latitude = location.latitude
    longtitude = location.longitude
    country = location.country


    data = (f"[+]Ip:{ip}\n")
    data += (f"Location info on {ip}\n")
    data += (f"Country:{country}\n")
    data +=(f"Region:{region}\n")
    data += (f"City:{city}\n")
    data += (f"Latitude:{latitude}\n")
    data += (f"Longtitude:{longtitude}\n")
    with open(filename+'.txt','w') as file:
        file.write(str(data))
    
    print((f"Data of IP:{ip} succesfully saved to {filename}.txt!")) 



def multi_save(filename,data):
    for info in data:
        with open(filename+'.txt','w')as file:
            file.write(str(data))    