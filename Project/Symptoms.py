class Symptoms:

    symptoms = {}

    def getSymptomKey(self, description):
        lower = description.lower()
        return Symptoms.symptoms[lower]


if __name__ == "__main__":
    s = Symptoms()
    print(s.getSymptomKey("head tremors"))


