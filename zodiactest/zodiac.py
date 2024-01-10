def define(dayx, monthy):
	day = dayx
	month = monthy
	zodiac = month
	if day > 31:
		zodaic = 0
	if month > 12:
		zodiac = 0
	if day >= 22:
		zodiac += 1
	if zodiac > 12:
		zodiac = 1
	return zodiac