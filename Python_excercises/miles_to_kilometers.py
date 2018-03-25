#Problem : Receive miles and convert to kilometers
#kilometers = miles * 1.60934
#Enter Miles 5,
# 5 miles equals 8.04 kilometers

print('Enter amount of miles to convert')
amount = input()
converted = float(amount) * 1.60934

print('{} miles equals {} kilometers'.format(amount,converted))
