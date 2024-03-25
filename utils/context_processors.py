def user_info(request):
    if request.user.is_authenticated:
        username = request.user.first_name
        return {'username': username}
    else:
        return {'username': None}
