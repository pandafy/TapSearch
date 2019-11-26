from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

from .helpers import *


class ListsDocumentView(generics.ListAPIView):
    """
    Provides a get method handler for listing,
    and post method hander for adding text.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def post(self, request, *args, **kwargs):
        input_text = request.data['text']
        docs = docufy(input_text)
        temp = []
        for doc in docs:
            temp.append(Document.objects.create(text=doc))
        commence_indexing(temp)
        return Response(
            status=status.HTTP_201_CREATED,
            data={'action': 'Success'}
        )


class SearchDocumentView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Words.objects.all()
    serializer_class = WordSerializer
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(
            SearchDocumentView,
            self).dispatch(
            request,
            *
            args,
            **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        input_text = request.data['word'].lower()
        try:
            word_obj = Words.objects.get(word=input_text)
            wf_qs = WordFrequencies.objects.filter(word_id=word_obj).select_related(
                'doc_id').values_list('doc_id')[:10]
            doc_qs = Document.objects.filter(id__in=wf_qs)

            data = DocumentSerializer(doc_qs, many=True).data
            mystatus = status.HTTP_200_OK

        except BaseException:
            data = "{'detail' : 'Not Found 404'}"
            mystatus = status.HTTP_204_NO_CONTENT

        return Response(
            status=mystatus,
            data=data
        )


# Create your views here.
@api_view(['GET', ])
def clear(request):
    Document.objects.all().delete()
    Words.objects.all().delete()
    return Response(
        status=status.HTTP_200_OK,
        data={"action": "Cleared all indexes."}
    )


def commence_indexing(my_list):
    """
    Uses helper functions to clean text and  indexes words.
    """
    for document in my_list:
        temp = indexify(document.text.lower())
        for key, value in temp.items():
            try:
                word_obj = Words.objects.get(word=key)
            except BaseException:
                word_obj = Words.objects.create(word=key)
            WordFrequencies.objects.create(
                word_id=word_obj,
                doc_id=document,
                frequency=value
            )
