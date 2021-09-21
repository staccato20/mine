# Generated by Django 3.2.5 on 2021-09-03 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_site_name', models.CharField(max_length=50)),
                ('book_url', models.URLField()),
            ],
            options={
                'ordering': ['book_site_name'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary_start_time', models.DateTimeField(verbose_name='시작시간')),
                ('diary_end_time', models.DateTimeField(verbose_name='마감시간')),
                ('diary_title', models.CharField(max_length=50, verbose_name='이벤트 이름')),
                ('diary_description', models.TextField(verbose_name='상세')),
            ],
            options={
                'verbose_name': '이벤트 데이터',
                'verbose_name_plural': '이벤트 데이터',
            },
        ),
    ]
