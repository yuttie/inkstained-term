from inkstained import palette


for k in palette:
    rgb_str = palette[k]
    r = int(rgb_str[1:3], 16)
    g = int(rgb_str[3:5], 16)
    b = int(rgb_str[5:7], 16)
    palette[k] = (r, g, b)

print(f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Ansi 0 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[0][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[0][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[0][0] / 0xff}</real>
	</dict>
	<key>Ansi 1 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[1][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[1][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[1][0] / 0xff}</real>
	</dict>
	<key>Ansi 10 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[10][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[10][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[10][0] / 0xff}</real>
	</dict>
	<key>Ansi 11 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[11][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[11][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[11][0] / 0xff}</real>
	</dict>
	<key>Ansi 12 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[12][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[12][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[12][0] / 0xff}</real>
	</dict>
	<key>Ansi 13 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[13][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[13][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[13][0] / 0xff}</real>
	</dict>
	<key>Ansi 14 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[14][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[14][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[14][0] / 0xff}</real>
	</dict>
	<key>Ansi 15 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[15][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[15][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[15][0] / 0xff}</real>
	</dict>
	<key>Ansi 2 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[2][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[2][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[2][0] / 0xff}</real>
	</dict>
	<key>Ansi 3 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[3][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[3][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[3][0] / 0xff}</real>
	</dict>
	<key>Ansi 4 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[4][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[4][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[4][0] / 0xff}</real>
	</dict>
	<key>Ansi 5 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[5][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[5][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[5][0] / 0xff}</real>
	</dict>
	<key>Ansi 6 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[6][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[6][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[6][0] / 0xff}</real>
	</dict>
	<key>Ansi 7 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[7][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[7][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[7][0] / 0xff}</real>
	</dict>
	<key>Ansi 8 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[8][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[8][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[8][0] / 0xff}</real>
	</dict>
	<key>Ansi 9 Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[9][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[9][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[9][0] / 0xff}</real>
	</dict>
	<key>Background Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette['background'][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette['background'][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette['background'][0] / 0xff}</real>
	</dict>
	<key>Badge Color</key>
	<dict>
		<key>Alpha Component</key>
		<real>0.5</real>
		<key>Blue Component</key>
		<real>0.0</real>
		<key>Color Space</key>
		<string>Calibrated</string>
		<key>Green Component</key>
		<real>0.0</real>
		<key>Red Component</key>
		<real>1</real>
	</dict>
	<key>Bold Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[0][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[0][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[0][0] / 0xff}</real>
	</dict>
	<key>Cursor Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette['cursor'][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette['cursor'][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette['cursor'][0] / 0xff}</real>
	</dict>
	<key>Cursor Guide Color</key>
	<dict>
		<key>Alpha Component</key>
		<real>0.25</real>
		<key>Blue Component</key>
		<real>1</real>
		<key>Color Space</key>
		<string>Calibrated</string>
		<key>Green Component</key>
		<real>0.9100000262260437</real>
		<key>Red Component</key>
		<real>0.64999997615814209</real>
	</dict>
	<key>Cursor Text Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette['background'][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette['background'][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette['background'][0] / 0xff}</real>
	</dict>
	<key>Foreground Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette['foreground'][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette['foreground'][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette['foreground'][0] / 0xff}</real>
	</dict>
	<key>Link Color</key>
	<dict>
		<key>Alpha Component</key>
		<real>1</real>
		<key>Blue Component</key>
		<real>0.67799997329711914</real>
		<key>Color Space</key>
		<string>Calibrated</string>
		<key>Green Component</key>
		<real>0.27000001072883606</real>
		<key>Red Component</key>
		<real>0.023000000044703484</real>
	</dict>
	<key>Selected Text Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[0][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[0][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[0][0] / 0xff}</real>
	</dict>
	<key>Selection Color</key>
	<dict>
		<key>Blue Component</key>
		<real>{palette[7][2] / 0xff}</real>
		<key>Green Component</key>
		<real>{palette[7][1] / 0xff}</real>
		<key>Red Component</key>
		<real>{palette[7][0] / 0xff}</real>
	</dict>
</dict>
</plist>""")
