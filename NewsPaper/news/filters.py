from django_filters import FilterSet, CharFilter, DateFilter
from .models import Post


# создаём фильтр
class PostFilter(FilterSet):
    # список полей для вывода фильтрации.
    # на что тут влияет имя переменной я не знаю
    # field_name - это, видимо, запрос, поле-в-модели__поле-по-ссылке__конечное-поле
    # lookup_expr - какое выражение применять к полю (icontains == "содержит")
    # label - текст, заголовок поля, человеческое названия для пользователя
    # author = CharFilter(field_name='author__user__username', lookup_expr='icontains', label='Пользователь')
    # create_time = DateFilter(field_name='date_time', lookup_expr='gte', label='Дата (yyyy-mm-dd)')

    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться
    # (т. е. подбираться) информация о товарах
    class Meta:
        model = Post

        # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)
        # я так понимаю, можно передать кортеж, а можно словарь, где уже кастомизировать фильтрацию
        # но не понятно, как, например, автора оставить также - выбором из списка
        # а рейтинг, например - сделать больше чем/меньше чем
        fields = ('author', 'time_post', 'author', 'name_news',)