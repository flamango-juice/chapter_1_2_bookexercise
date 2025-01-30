import math
# 1.9.1 Should I use DeepSeek???

# 1.9.2
print(round(42.5), round(43.5), round(44.5))

# 1.9.3
print(2++2) # Sends warning but does the addition correctly.
# 4 2 - SyntaxError: invalid syntax
# round(41.5 - SyntaxError: '(' was never closed

# 1.9.4
print(type(765)) # guess is an int. correct
print(type(2.718)) # guess is a float. correct
print(type("2 pi")) # guess is string correct
print(type(abs(-7))) # int correct
print(type(abs(-7.0))) # float correct
print(type(abs)) # func wrong
print(type(int)) # func wrong
print(type(type)) # func wrong

# 1.9.5
m = 42
min_to_sec = (m * 60) + 42

km = 10
km_to_mi = km / 1.609344

spm = min_to_sec / km_to_mi

mspm = spm / 60
mmmmm = spm // 60
msec = (mspm - mmmmm) * 60

hour = (min_to_sec / 60**2)
mph = km_to_mi / hour
print(f"""
Time: {min_to_sec:d} seconds
Length (10km in mi): {km_to_mi:.2f} miles
Pace (seconds): {spm:.2f} seconds
Pace (minutes + seconds): {mmmmm:.0f} minutes, {msec:.0f} seconds
Pace (mph): {mph:.0f} miles per hour
""")