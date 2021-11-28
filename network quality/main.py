import subprocess
import re
newline = '\n'

quality = subprocess.run(['/usr/bin/networkQuality'], capture_output=True, text=True).stdout

theUploadMatch = re.search('Upload capacity: ([0-9\.]+) Mbps', quality)
theUpload = theUploadMatch.group(1)
theDownloadMatch = re.search('Download capacity: ([0-9\.]+) Mbps', quality)
theDownload = theDownloadMatch.group(1)
theResponsiveMatch = re.search('Responsiveness: (.*?)$', quality)
theResponsive = theResponsiveMatch.group(0)

theUpround = str(round(float(theUpload)))
theDownround = str(round(float(theDownload)))

theOutput = (f'{theDownround} :icloud.and.arrow.down: {theUpround} '
			 f':icloud.and.arrow.up:{newline}---{newline}{theResponsive}')

print (theOutput)


