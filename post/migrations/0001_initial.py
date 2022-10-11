# Generated by Django 4.0.4 on 2022-10-10 01:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_desc', models.CharField(max_length=10024)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availablepost', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_desc', models.CharField(max_length=10024)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availablecommentuser', to=settings.AUTH_USER_MODEL)),
                ('post_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availablecomment', to='post.posttable')),
            ],
        ),
    ]