import infermedica_api

class Api:

    def __init__(self, sex, age):
        self.sex = sex
        self.age = age

    def get_conditions(self, sex, age, symptoms):
        '''
        Return a list of possible conditions by the symptoms

        :param sex: string
                can only be "female" or "male"
        :param age: int
        :param symptoms: list of strings
                list of symptoms
        :rtype: list of strings
                list of possible conditions
        '''
        infermedica_api.configure(app_id='2f25564c', app_key='bf70a95520b458fe0e69974f34d19a22')
        api = infermedica_api.get_api()
        # Create diagnosis object with initial patient information.
        request = infermedica_api.Diagnosis(sex=sex, age=age)
        for i in range(len(symptoms)):
            request.add_symptom(symptoms[i], 'present')

        request = api.diagnosis(request)
        result = []
        # get list of possible conditions
        for i in range(max(len(request.conditions[i]), 3)):
           result.append(request.conditions[i]['name'])
        return result

'''
if __name__ == '__main__':
    c = Api("male", 20)
    conditions = c.get_conditions("male", 20, ['s_11', 's_97', 's_107'])
    print(conditions)
'''

