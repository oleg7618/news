

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NewsPaper', '0002_rename_rating_comment_comment_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subscribed_users',
            field=models.ManyToManyField(related_name='subscribed_categories', to=settings.AUTH_USER_MODEL),
        ),
    ]
