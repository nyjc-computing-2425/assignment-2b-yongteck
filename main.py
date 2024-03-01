num = input('Enter a number (decimal only): ')
# type your code here
place = num.find(".")
dp = len(num) - place - 1 #extra 1 is needed as len is not 0 indexed 
# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
