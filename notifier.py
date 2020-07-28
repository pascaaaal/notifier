import sys
import subprocess
import os
import time
import pychromecast
import argparse

env_vars = {}

#Just loads all values from the data file
def load_data(path):
        result = []
        lines = open(path, 'r').readlines()

        for line in lines:
                if line[0] is '#' or not line.strip():
                        continue
                result.append([line.split()[0], 0, line.split()[1], False])
        return result

#Loads all config vars
def load_config(path):
	lines = open(path, 'r').readlines()
	for line in lines:
		if line[0] is '#' or not line.strip():
			continue
		key, value = line.strip().split('=', 1)
		env_vars[key.strip()] = value.strip()

parser = argparse.ArgumentParser()

parser.add_argument('-c', '--config', help='Provides the config file', required=True)
parser.add_argument('-d', '--data', help='Provides the data file', required=True)

args = parser.parse_args()

list = load_data(args.data)
load_config(args.config)

while True:
	ips = []
	proc = subprocess.Popen(['fping', '-d', '-i 1', '-r 2', '-a', '-g', env_vars['subnet_addr']], stdout=subprocess.PIPE, stderr=open(os.devnull, 'w'))

	while True:
		line = proc.stdout.readline().decode('utf-8')
		if not line:
			break
		ips.append(line.strip())
	for i in list:
		if i[0] in ips:
			i[1] = time.time()
			if not i[3]:
				#This is not async because your chromecast devace cant handle 2 Audiostreams
				print('[+]', i[0], 'is alive')
				cast = pychromecast.Chromecast(env_vars['chromecast_addr'])
				cast.wait()
				mc = cast.media_controller
				mc.play_media(i[2], 'audio/mp3')
				mc.stop()
				i[3] = True
				print('[*]', 'Audio sent')
		else:
			if time.time() - i[1] >= int(env_vars['timeout']) and i[3]:
				print('[-]', i[0], 'is not alive')
				i[3] = False

