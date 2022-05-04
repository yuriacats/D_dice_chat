"""docstring
Pollsの見栄えの部分
"""
from django.http import HttpResponse


def index(request) -> HttpResponse:
    """docstring
    Viewの部分/pollだけの時のAPIのレスポンス
    """
    return HttpResponse("Hello,world. こんにちは")


def details(request, question_id):
    """docstring
    Viewの部分/pollだけの時のAPIのレスポンス
    """
    response = "あなたは、この質問を見ています %s"
    return HttpResponse(response % question_id)


def results(request, question_id):
    """docstring
    Viewの部分/pollだけの時のAPIのレスポンス
    """
    response = "あなたは、この質問の答えを見ています %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    """docstring
    Viewの部分/pollだけの時のAPIのレスポンス
    """
    return HttpResponse("あなたはこの質問に投票しようとしています %s" % question_id)