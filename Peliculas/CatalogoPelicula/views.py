# from django.shortcuts import render

# Create your views here.


def vista(opcion):
    if opcion:
        return ('Es true')
    else:
        return ('Es false')
    # if False:
    # 	return ('Es False')
    # else:
    # 	return ('Es True')
