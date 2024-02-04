
expected = 90

age = int(input("Enter your age: "))

left = expected - age

#assume 52 weeks for year, 365 days and 12 months

lifeInWeeks =  left * 52
lifeInmonths = left*12
lifeIndays = left*365

print(f"you have {lifeInmonths}: Months, {lifeInWeeks}: weeks, {lifeIndays }: days to live, Enjoy!")