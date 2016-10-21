# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-19 19:29
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20161011_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendapage',
            name='mtg_media',
            field=wagtail.wagtailcore.fields.StreamField((('full_video_url', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('full_audio', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)), ('mtg_transcript', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False))), default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agendapage',
            name='agenda',
            field=wagtail.wagtailcore.fields.StreamField((('agenda_item', wagtail.wagtailcore.blocks.StreamBlock((('item_title', wagtail.wagtailcore.blocks.TextBlock()), ('item_text', wagtail.wagtailcore.blocks.TextBlock()), ('mtg_doc', wagtail.wagtailcore.blocks.StructBlock((('mtg_doc_upload', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=True)), ('submitted_late', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Submitted Late', required=False)), ('heldover', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Held Over', required=False)), ('heldover_from', wagtail.wagtailcore.blocks.DateBlock(help_text='Held Over From', required=False))))), ('item_audio', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False))))),)),
        ),
    ]