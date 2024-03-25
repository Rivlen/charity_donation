def user_info(request):
    if request.user.is_authenticated:
        username = request.user.first_name
        return {'username': username, 'is_superuser': request.user.is_superuser}
    else:
        return {'username': None}
