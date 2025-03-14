from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def company_details(request):
    return Response({'company_name': 'Веселые бегуны',
                     'slogan':'Бежим посмеиваясь',
                     'contacts': 'г. Сосновск, ул. Сосновая 16'})
