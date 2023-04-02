from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

from joblib import load
model = load('./savedModels/model_ashu.joblib')

def predictor(request):
    if request.method == 'POST':
        country_code = request.POST['country_code']
        gender = request.POST['gender']
        medicare_participation = request.POST['medicare_participation']
        place_of_service = request.POST['place_of_service']
        hcpcs_drug_indicator = request.POST['hcpcs_drug_indicator']

        #require operation 
        number_of_medicare_beneficiaries = request.POST['Number of Medicare Beneficiaries']
        average_submitted_charge_amount = request.POST['Average Submitted Charge Amount']
        average_medicare_standardized_amount = request.POST['Average Medicare Standardized Amount']

        #multiple values to be send
        credentials_provider = request.POST['credentials_provider']
        state_code_provider = request.POST['state_code_provider']
        provider_type = request.POST['provider_type']

        credentials = []
        for i in range(0,12):
            if i==int(credentials_provider):
                credentials.append(1)
            else:
                credentials.append(0)
        
        state_code = []
        for i in range(0,14):
            if i==int(state_code_provider):
                state_code.append(1)
            else:
                state_code.append(0)

        provider = []
        for i in range(0,26):
            if i==int(provider_type):
                provider.append(1)
            else:
                provider.append(0)
        
        mean_dict = {'mean': {'number_of_medicare_beneficiaries': 89.80931,
                            'average_submitted_charge_amount': 354.55045081579567,
                            'average_medicare_standardized_amount': 78.03069297594605},
                            'std': {'number_of_medicare_beneficiaries': 1109.616901666514,
                            'average_submitted_charge_amount': 1062.6082712547693,
                            'average_medicare_standardized_amount': 200.04545774030595}}
        
        number_of_medicare_beneficiaries = (int(number_of_medicare_beneficiaries) - mean_dict['mean']['number_of_medicare_beneficiaries'])/mean_dict['std']['number_of_medicare_beneficiaries']
        average_submitted_charge_amount = (int(average_submitted_charge_amount) - mean_dict['mean']['average_submitted_charge_amount'])/mean_dict['std']['average_submitted_charge_amount']
        average_medicare_standardized_amount = (int(average_medicare_standardized_amount) - mean_dict['mean']['average_medicare_standardized_amount'])/mean_dict['std']['average_medicare_standardized_amount']

        list = [int(country_code), int(gender), int(medicare_participation), int(place_of_service), int(hcpcs_drug_indicator), number_of_medicare_beneficiaries, average_submitted_charge_amount, average_medicare_standardized_amount]
        list.extend(credentials)
        list.extend(state_code)
        list.extend(provider)
        # print('list',list)
        y_pred = model.predict([list])
        # print('y_pred:', y_pred)
        if y_pred[0] == 0:
            y_pred = 'Non Fraud'
        else:
            y_pred = 'Fraud'
        return render(request, 'form.html', {'result' : y_pred})
    return render(request, 'form.html')
