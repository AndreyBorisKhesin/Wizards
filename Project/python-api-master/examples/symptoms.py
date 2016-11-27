from __future__ import print_function
import config

config.setup_examples()
import infermedica_api


if __name__ == '__main__':
    api = infermedica_api.get_api()

    print('Symptoms list:')
    print(api.symptoms_list(), '\n')

    list = api.symptoms_list()
    dict = {}
    for i in range(len(list)):
       if list[i]["name"] != "":
           dict[list[i]["name"]] = list[i]["id"]
    print(dict)
    """

    print('Symptom details:')
    print(api.symptom_details('s_56'), end="\n\n")

    print('Symptom details (with children):')
    print(api.symptom_details('s_551'), end="\n\n")

    print('Non-existent symptom details:')
    print(api.symptom_details('fail_test'))
    """
