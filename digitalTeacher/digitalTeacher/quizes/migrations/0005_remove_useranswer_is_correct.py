# Generated by Django 5.1.1 on 2024-09-19 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0004_rename_answer_useranswer_selected_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='is_correct',
        ),
    ]
