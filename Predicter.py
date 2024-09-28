class Predicter:

    def predict(self, Factors):
        delay = 0

        #turns
        delay += Factors.leftTurn * 2 * (Factors.traffic * 0.1)
        delay += Factors.leftTurn * 1 * (Factors.traffic * 0.1)

        #distance
        delay += Factors.distance * 2 * (Factors.traffic * 0.5)

        #weather
        if Factors.weather == "rain" or Factors.weather == "Rain":
            delay *= 1.2
        elif Factors.weather == "snow" or Factors.weather == "Snow":
            delay *= 1.4

        #day of the week
        if Factors.day == "Weekday" or Factors.day == "weekday":
            delay *= 1.0
        if Factors.day == "Weekend" or Factors.day == "weekend":
            delay *= 0.9

        if (7 < Factors.time < 9 or 18 < Factors.time < 21) and (Factors.day == "Weekday" or Factors.day == "weekday"):
            delay *= 1.2

        delay = round(delay)
        return delay