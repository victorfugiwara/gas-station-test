from django.shortcuts import render

def index(request):
    messages = []
    manual = ''
    show_data = False

    if request.method == 'POST':
        show_data = request.POST.get('show_data', False)
        text_file = request.FILES.get('text_file')
        if text_file:
            for line in text_file:
                messages.append(validateTestString(line.decode("utf-8"), show_data))

        manual = request.POST.get('manual_test', '')
        if manual:
            messages.append(validateTestString(manual, show_data))

    context = {
        'messages': messages,
        'manual': manual,
        'show_data': show_data
    }

    return render(request, 'index.html', context)


def validateTestString(test, show_data):
    test = test.replace('"', '').replace("'", "").rstrip('\r\n')
    array_values = test.split(',')
    n = int(array_values[0])
    stations = len(array_values)-1
    if n != stations:
        return 'Invalid number of stations. N={} and array contains {} station(s)'.format(n, stations)
    else:
        index_start = GasStation(test)
        if index_start:
            if show_data:
                return '{} - {}'.format(test, index_start)
            else:
                return index_start
        else:
            if show_data:
                return '{} - Impossible'.format(test)
            else:
                return 'Impossible'


def GasStation(strArr):
    array_values = strArr.split(',')
    total = int(array_values[0])

    for initial in range(1, total+1):
        gas = 0
        stations = array_values[initial:total+1]
        stations.extend(array_values[1:initial])

        for item in stations:
            station = item.split(':')
            gas_here = int(station[0])
            gas_to_next = int(station[1])

            gas += gas_here
            gas -= gas_to_next
            if gas < 0:
                break

        if gas >= 0:
            return initial
            
    return None
