# Generated by Django 3.2 on 2023-01-26 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='event',
            name='how_long',
            field=models.SmallIntegerField(default=90, verbose_name='How long (minutes)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='email',
            field=models.EmailField(default='teste@email.com', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Is active'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='event',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='events',
            field=models.ManyToManyField(blank=True, to='register_events.Event', verbose_name='Events'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Updated at'),
        ),
    ]
