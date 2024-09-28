from Factors import Factors
from Predicter import Predicter

factors = Factors(1,2,3,2, "Rain", "Weekday", 7)

predicter = Predicter()

delay = predicter.predict(factors)

print(delay)