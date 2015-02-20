#beyond ingenious
s = 'azcbobobegghakl'
curString = s[0]
longest = s[0]
for i in range(1, len(s)):
	#curString[-1] gets you the last char
    if s[i] >= curString[-1]:
        curString += s[i]
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]
print 'Longest substring in alphabetical order is:', longest