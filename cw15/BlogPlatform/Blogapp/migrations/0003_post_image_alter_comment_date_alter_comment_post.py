# Generated by Django 4.2.3 on 2023-07-14 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Blogapp", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="post_images/"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="Blogapp.post",
            ),
        ),
    ]