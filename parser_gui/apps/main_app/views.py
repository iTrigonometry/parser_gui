from django.shortcuts import render


# главная страница приложения main_app
# первое что видит пользователь
def index(request):
    """Main page
    Returns:
        [render] -- [Main site's page]
    """
    return render(request, 'main_app/index.html')


# TODO выяснил что select не дает делать обычные POST, как бы это заменить
def test(request):
    """для тестирования функций
    Arguments:
        request {request} -- standart parametr
    Returns:
        render -- site's page
    """
    site = request.POST['zapros']
    return render(request, 'main_app/test.html', {'tender_site': site}) # noqa
