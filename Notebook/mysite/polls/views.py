from django.shortcuts import render, redirect
import pandas as pd
import pickle

def index_func(request):
    res = 0
    if request.method == 'POST':
        name = request.POST['Name']
        repute = request.POST['repute']
        height = request.POST['Height']
        width = request.POST['Width']
        weight = request.POST['Weight']
        material = request.POST['material'] # select
        basePrice = request.POST['basePrice']
        basePriceShipping = request.POST['basePriceShipping']
        international = request.POST['international']
        expressShipment= request.POST['expressShipment']
        installments = request.POST['installments']
        transport = request.POST['Transport']
        fragile = request.POST['Fragile']
        customer = request.POST['cust']
        remote = request.POST['remote']
        waiting = request.POST['waiting']

        if name != "":
            df = pd.DataFrame(columns=['Artist Reputation', 'Height', 'Width',
                               'Weight', 'Material', 'Price Of Sculpture', 'Base Shipping Price',
                               'International', 'Express Shipment', 'Installation Included',
                               'Transport', 'Fragile', 'Customer Information', 'Remote Location',
                               'Waiting time'])

            df2 = {'Artist Reputation': float(repute), 'Height': float(height), 'Width': float(width),
                   'Weight': float(weight), 'Material': int(material), 'Price Of Sculpture':
                    float(basePrice), 'Base Shipping Price': float(basePriceShipping),'International':
                   int(international), 'Express Shipment': int(expressShipment), 'Installation Included':
                   int(installments),'Transport': int(transport), 'Fragile': int(fragile),
                   'Customer Information': int(customer), 'Remote Location': int(remote),'Waiting time':
                   float(waiting)}

            df = df.append(df2, ignore_index=True)
            # load the model from disk
            filename1 = 'polls/Artist.pickle'
            loaded_model = pickle.load(open(filename1, 'rb'))
            res = loaded_model.predict(df)
            print(res)

        else:
            return redirect('homepage')
    else:
        pass

    return render(request, "index.html", {'response': res})