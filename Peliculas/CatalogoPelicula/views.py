# from django.shortcuts import render

# Create your views here.


def vista(opcion):
    if opcion:
        return 'Es True'
    else:
        return 'Es False'

    # if False:
    #    print('Es False')
    # else:
    #    print('Es True')
