#! /usr/local/bin/python3

import os
import plistlib

xcode_info = '/Applications/Xcode.app/Contents'
plug_in_path = os.environ["HOME"] + '/Library/Application Support/Developer/Shared/Xcode/Plug-ins/'
uuid_key = 'DVTPlugInCompatibilityUUID'
plugin_key = 'DVTPlugInCompatibilityUUIDs'

#get the uuid of xcode configuration
with open(xcode_info + '/Info.plist', 'rb') as fp:
	temp = plistlib.load(fp)
	uuid = temp[uuid_key]

#get plugins' paths 
plugin_paths = []
plugin_names = []
temp_path = os.listdir(plug_in_path)
for path in temp_path:
	temp_name = os.path.splitext(path)
	if ('.xcplugin' == temp_name[1]):
		plugin_paths.append(plug_in_path + path + '/Contents/')
		plugin_names.append(temp_name[0])

#change plugins' uuids
update_list = []
for index in range(len(plugin_paths)):
	temp_path = plugin_paths[index] + 'Info.plist'
	with open(temp_path, 'rb+') as fp:
		temp = plistlib.load(fp)
		if (uuid in temp[plugin_key]):
			print(plugin_names[index], 'is already latest.')
		else:
			update_list.append(plugin_name[index])
			temp[plugin_key].append(uuid)
			fp.seek(0)
			plistlib.dump(temp, fp)
			print(plugin_names[index], 'is updated!')

print('\nfinished!', len(update_list), 'plugin(s) have been updated!')
