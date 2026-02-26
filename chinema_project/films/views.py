from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Film
from .seralizers import FilmSerializer, FilmDetailSerializer



@api_view(['GET'])
def film_detail_api_view(request, id):
    try:
        film = Film.objects.get(id=id)
    except Film.DoesNotExist:
        return Response(
                data={'error': 'Film not found'},
                status=status.HTTP_404_NOT_FOUND
        )
    data = FilmDetailSerializer(film).data
    return Response(data=data)



@api_view(['GET'])
def film_list_api_view(request):
    #step1: Collect films from database (queryset)
    films = Film.objects.all()


    #step2: Reformat (serialize) films
    data = FilmSerializer(films, many=True).data


    #step3: Return Response
    return Response(
        data=data,

    )
    