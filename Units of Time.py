#v1
def secondsConverter(minute, hour, day):
  h  = hour * 3600
  m = minute * 60 
  d = day * 3600 * 24
  result = h + m + d
  print('This amounts to  {} seconds.'.format(result))
  
secondsConverter(43, 12, 2)  

#v2
def secondsConverter():
  hour = float(input('Enter hours: '))
  minute = float(input("Enter minutes: "))
  day = float(input('Enter days: '))
  h  = hour * 3600
  m = minute * 60 
  d = day * 3600 * 24
  result = h + m + d
  print('This amounts to  {} seconds.'.format(result))
   
secondsConverter() 