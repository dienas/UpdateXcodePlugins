# UpdateXcodePlugins
Update the configration of Xcode plugins

function:
This python script use for enable Xcode's plugins after Xcode updating.
The reason of the Plugins becoming invalid is that the Plugin's DVTPlugInCompatibilityUUIDs has not suited to Xcode when Xcode updated.

Implenment:
Step 1:
Check for a value whose key is "DVTPlugInCompatibilityUUID" in Xcode's Info.plist file, usually in path "/Applications/Xcode.app/Contents/Info.plist".

Step 2:
Add this value to the key named "DVTPlugInCompatibilityUUIDs" in every Xcode Plugin's Info.plist, usually in path "~/Library/Application Support/Developer/Shared/Xcode/Plug-ins/".

Step 3:
After this, restart the Xcode add choose "load bundle" to enable Plugins.
