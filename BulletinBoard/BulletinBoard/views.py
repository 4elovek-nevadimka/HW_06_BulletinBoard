from django.shortcuts import redirect


def go_to_board(request):
    return redirect('/board/')
