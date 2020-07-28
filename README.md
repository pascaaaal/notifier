# notifier
This is a small script to send a notification via your Google Home when a specific IP enters your Network.
# Installation
<code>sudo bash <(curl -s https://raw.githubusercontent.com/pascaaaal/notifier/master/install.sh)</code>
# Requirements
<li>Python 3.7</li>
<li>fping</li>
<li>pychromecast</li>

# Usage
You can edit the data.txt it is placed in <code>/etc/notifier/data.txt</code>.
The Scheme <code>ip mp3_url</code>
So for example you have the ip adress <code>192.168.2.100</code>, and you want the url <code>https://example.com/exmaple.mp3</code>. You're line would be:
<br/>
<code>192.168.2.100 https://example.com/exmaple.mp3</code>

# Configuration
To use the script properly, you have to edit the config.txt. It is placed in <code>/etc/notifier/config.txt</code>.
<br />
The value <code>subnet_addr</code> is the subnet scheme of your network.
<br/>
The value <code>chromecast_addr</code> represents the ip address of your chromecast device.
<br/>
The value <code>timeout</code> is the the timeout how long it takes that the system marks a IP as "at home". This is beacause your device does not respond everytime.
