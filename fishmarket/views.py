from django.shortcuts import render
from .forms import FishMarketForm  # Assuming you have a form associated with your model
import joblib,os
from django.conf import settings



def predict(request):
    form = FishMarketForm()
    value = 'Enter Inputs and then click on Predict'
    if request.method == 'POST':
        form = FishMarketForm(request.POST)

        if form.is_valid():
            w = form.cleaned_data['weight']
            l1 = form.cleaned_data['length1']
            l2 = form.cleaned_data['length2']
            l3 = form.cleaned_data['length3']
            h = form.cleaned_data['height']
            wi = form.cleaned_data['width']
            model_path = os.path.join(settings.BASE_DIR, 'fishmarket', 'random_forest_model.pkl')
            with open(model_path, 'rb') as file:
                model = joblib.load(file)
                y_pred = model.predict([[w, l1, l2, l3, h, wi]])
                value = int(y_pred[0])

                labels = {
                            0: 'Bream',
                            1: 'Parkki',
                            2: 'Sweet',
                            3: 'Pike',
                            4: 'Roach',
                            5: 'Smelt',
                            6: 'Whitefish'
                        }
                value = labels.get(value, 'Unknown')  
        
            
    return render(request, 'result.html', {'form': form, 'value': value})

            