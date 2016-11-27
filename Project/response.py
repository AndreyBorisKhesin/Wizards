import Person
import Api
import Symptoms


class Response:
	people = []

	@staticmethod
	def generateresponse(phonenumber, textmessage, timestamp):
		if textmessage is None:
			return
		textmessage1 = textmessage.lower()
		found = False
		# Check if the person exists in the list of people
		for p in range(len(Response.people)):
			if Response.people[p].phone_number == phonenumber:
				found = True
				# current person
				cpeep = Response.people[p]
		if (not found):
			newp = Person.Person(phonenumber)
			Response.people.append(newp)
			cpeep = newp
		#finds all symptoms in hashes in text
		i = 0
		while i < len(textmessage1):
			if textmessage1[i] == "#":
				newsymp = ""
				j = i + 1
				while j < (len(textmessage1)):
					newsymp = newsymp + textmessage1[j]
					if (textmessage1[j] == "#"):
						if newsymp != "#":
							l = len(newsymp) - 1
							newsymp = newsymp[0:l].lower()
							if not cpeep.symptoms.__contains__(newsymp):
								cpeep.symptoms.append(newsymp)
							i = j + 1
							break
					j += 1
			i += 1
		if cpeep.gender == "":
			if textmessage1 == "f" or textmessage1 == "m":
				cpeep.gender = textmessage1
			else:
				return "What is your gender? Please enter F for Female and M for Male"	
		if cpeep.gender != "" and cpeep.age == -1:
			try:
				age = int(textmessage1)
				if age >= 0:
					cpeep.age = age
				else:
					return "How old are you?"
			except ValueError:
				return ("How old are you?")
		if cpeep.gender != "" and cpeep.age >= 0:
			if textmessage1[-2:] == "**":
				if len(cpeep.symptoms) == 0:
					return "Please enter at least one symptom."
				keys = []
				for symptom in cpeep.symptoms:
					keys.append(Symptoms.Symptoms.getSymptomKey(symptom))
				a = Api.Api("male" if cpeep.gender == "m" else "female",
						cpeep.age)
				conditions = a.get_conditions(
						"male" if cpeep.gender == "m" else "female",
						cpeep.age,
			   		keys)
				return "In order of likelyhood, you might have one of the following:\n" + conditions[0] + ("" if len(conditions) < 2 else (", " + conditions[1])) + ("" if len(conditions) < 3 else (", " + conditions[2])) + "."
			else:
				return "Please enter all relevant symptoms in between two hashes (e.g. #headache#).\nEnd your message with ** to receive your diagnosis. (DISCLAIMER: This is not to be used as medical advice. For a complete diagnosis, it is advised that you seek professional help.)"
