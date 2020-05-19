from wagtail.core import blocks


class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text="Enter the title")
    text = blocks.TextBlock(required=True, help_text="Enter text")

    class Meta:
        templates = 'streams/title_and_text_block.html'
        icon = "edit"
        label = "Title & Text"
