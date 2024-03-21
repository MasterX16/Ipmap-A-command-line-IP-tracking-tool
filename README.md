# Ipmap

## About 
This is a simple command line tool written in Python that allows geolocation of IP addresses directly from your terminal. It has been tested on Kali Linux only for now, though it should work for Debian-based systems as well as for other Linux-based systems.

## Installation

```bash
git clone https://github.com/MasterX16/Ipmap-A-command-line-IP-tracking-tool
cd Ipmap
pip install -r requirements.txt
chmod +x setup.sh
sudo ./setup.sh
ipmap -h
Now the file is added to PATH
```
## Features
Geolocation of single ip  <br />
Mapping the location to a .html file which can be later viewed in a web browser.Interactive map done using folium library with markers.<br />
Marking location of multiple IP's on one interactive map with markers <br />
Geolocation of ip lists and wordlists,which are txt files with ips   <br />
Saving geolocation to txt and json files   <br />

## License
This project is released under the MIT License.See the [LICENSE](https://github.com/MasterX16/Ipmap-A-command-line-IP-tracking-tool/LICENSE) file for more.
