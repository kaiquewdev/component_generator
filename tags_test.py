'''Tags Test'''

import tags
import unittest

class NFZTest(unittest.TestCase):
    def setUp(self):
        self.nfz = tags.NFZ()

    def test_nfz_instantiation(self):
        self.assertEqual(self.nfz.__class__,tags.NFZ)

    def test_nfz_utf_without_value(self):
        self.assertEqual(self.nfz.UTF_WITHOUT_VALUE.template,'<$tname $tattrs_fslash>')

    def test_nfz_ctf_template_value(self):
        self.assertEqual(self.nfz.CTF.template,'<$tname $tattrs>$tvalue</$tname>')

    def test_nfz_ctf_without_attrs_template(self):
        self.assertEqual(self.nfz.CTF_WITHOUT_ATTRS.template,'<$tname>$tvalue</$tname>')

class TagTest(unittest.TestCase):
    def setUp(self):
        self.raw_tag = tags.Tag(name='p')

    def test_paragraph_instantiation(self):
        self.assertEqual(self.raw_tag.__class__,tags.Tag)

    def test_paragraph_html(self):
        self.assertEqual(self.raw_tag.html('Hello from taggler'),'<p>Hello from taggler</p>')

    def test_paragraph_class(self):
        self.assertEqual(tags.Tag({'class':'message'},'p').html('Hello from taggler'),'<p class="message">Hello from taggler</p>')

class DivTest(unittest.TestCase):
    def setUp(self):
        self.div = tags.Div()

    def test_div_instantiation(self):
        self.assertEqual(self.div.__class__,tags.Div)

    def test_div_html(self):
        self.assertEqual(self.div.html('Div model'),'<div>Div model</div>')

    def test_div_class(self):
        self.assertEqual(tags.Div({'class':'holder'}).html('Div model'),'<div class="holder">Div model</div>')

class ImageTest(unittest.TestCase):
    def setUp(self):
        self.image = tags.Image({'src':'//placeholder.it/50x50/'})

    def test_image_instantiation(self):
        self.assertEqual(self.image.__class__,tags.Image)

    def test_image_html(self):
        self.assertEqual(self.image.html(),'<img src="//placeholder.it/50x50/"/>')

    def test_image_class(self):
        self.assertEqual(tags.Image({'class':'outer-figure-holder','src':'//placeholder.it/50x50/'}).html(),'<img class="outer-figure-holder" src="//placeholder.it/50x50/"/>')

class SpanTest(unittest.TestCase):
    def setUp(self):
        self.span = tags.Span()

    def test_span_instantiation(self):
        self.assertEqual(self.span.__class__,tags.Span)

    def test_span_html(self):
        self.assertEqual(self.span.html('Peace into the heart'),'<span>Peace into the heart</span>')

class AnchorTest(unittest.TestCase):
    def setUp(self):
        self.anchor = tags.Anchor({'class':'anchor-point','href':'http://kaiquesilva.com.br'})

    def test_anchor_instantiation(self):
        self.assertEqual(self.anchor.__class__,tags.Anchor)

    def test_anchor_html(self):
        self.assertEqual(self.anchor.html('Anchor value'),'<a class="anchor-point" href="http://kaiquesilva.com.br">Anchor value</a>')

class AbbrTest(unittest.TestCase):
    def setUp(self):
        self.abbr = tags.Abbr({"title":"Feel The Hacking"})

    def test_abbr_instantiation(self):
        self.assertEqual(self.abbr.html('FTH'),'<abbr title="Feel The Hacking">FTH</abbr>')

    def test_abbr_html(self):
        self.assertEqual(tags.Abbr({"title":"Feel The Hacking","class":"feel-steps"}).html('FTH'),'<abbr class="feel-steps" title="Feel The Hacking">FTH</abbr>')

class AddressTest(unittest.TestCase):
    def setUp(self):
        self.address = tags.Address()

    def test_address_instantiation(self):
        self.assertEqual(self.address.html('Av. Dr. Ministro Xavier, 0'),'<address>Av. Dr. Ministro Xavier, 0</address>')

class AreaTest(unittest.TestCase):
    def setUp(self):
        self.area = tags.Area({'shape':'rect','coords':'0,0,82,126','href':'sum.html','alt':'Sun'})

    def test_area_instantiation(self):
        self.assertEqual(self.area.html(),'<area alt="Sun" coords="0,0,82,126" href="sum.html" shape="rect">')

class ArticleTest(unittest.TestCase):
    def setUp(self):
        self.article = tags.Article()

    def test_article_instantiation(self):
        self.assertEqual(self.article.html('Text inside of the article tag'),'<article>Text inside of the article tag</article>')

class AsideTest(unittest.TestCase):
    def setUp(self):
        self.aside = tags.Aside()

    def test_aside_instantiation(self):
        self.assertEqual(self.aside.html('Text inside of aside tag'),'<aside>Text inside of aside tag</aside>')

class AudioTest(unittest.TestCase):
    def setUp(self):
        self.audio = tags.Audio({'controls':''})

    def test_audio_instantiation(self):
        self.assertEqual(self.audio.html('Text inside of audio tag'),'<audio controls>Text inside of audio tag</audio>')

class SourceTest(unittest.TestCase):
    def setUp(self):
        self.source = tags.Source({'src':'horse.ogg','type':'audio/ogg'})

    def test_source_instantiation(self):
        self.assertEqual(self.source.html(),'<source src="horse.ogg" type="audio/ogg">')

class BoldTest(unittest.TestCase):
    def setUp(self):
        self.bold = tags.Bold()

    def test_bold_instantiation(self):
        self.assertEqual(self.bold.html('this is a bold text'),'<b>this is a bold text</b>')

class ParagraphTest(unittest.TestCase):
    def setUp(self):
        self.paragraph = tags.Paragraph()

    def test_paragraph_html(self):
        self.assertEqual(self.paragraph.html('this is a p tag'),'<p>this is a p tag</p>')

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.base = tags.Base({'href':'http://kaiquesilva.com.br/resources/','target':'_blank'})

    def test_base_instantiation(self):
        self.assertEqual(self.base.__class__,tags.Base)
        
    def test_base_html(self):
        self.assertEqual(self.base.html(),'<base href="http://kaiquesilva.com.br/resources/" target="_blank">')

class BodyTest(unittest.TestCase):
    def setUp(self):
        self.body = tags.Body()

    def test_body_instantiation(self):
        self.assertEqual(self.body.__class__,tags.Body)

    def test_body_html(self):
        self.assertEqual(self.body.html('Sample test'),'<body>Sample test</body>')

class HeadTest(unittest.TestCase):
    def setUp(self):
        self.head = tags.Head()

    def test_head_instantiation(self):
        self.assertEqual(self.head.__class__,tags.Head)

    def test_head_html(self):
        self.assertEqual(self.head.html(),'<head></head>')

class LinkTest(unittest.TestCase):
    def setUp(self):
        self.link = tags.Link({'href':'style.css','type':'application/stylesheet'})

    def test_link_instantiation(self):
        self.assertEqual(self.link.__class__,tags.Link)

    def test_link_html(self):
        self.assertEqual(self.link.html(),'<link href="style.css" type="application/stylesheet"/>')

class ScriptTest(unittest.TestCase):
    def setUp(self):
        self.script = tags.Script({'src':'main.js'})

    def test_script_instantiation(self):
        self.assertEqual(self.script.__class__,tags.Script)

    def test_script_html(self):
        self.assertEqual(self.script.html(),'<script src="main.js"/>')

class MetaTest(unittest.TestCase):
    def setUp(self):
        self.meta = tags.Meta({'name':'robots','content':'NONE,NOARCHIVE'})

    def test_meta_instantiation(self):
        self.assertEqual(self.meta.__class__,tags.Meta)

    def test_meta_html(self):
        self.assertEqual(self.meta.html(),'<meta content="NONE,NOARCHIVE" name="robots"/>')

class HeaderOneTest(unittest.TestCase):
    def setUp(self):
        self.h1 = tags.Header(1)

    def test_h1_instantiation(self):
        self.assertEqual(self.h1.__class__,tags.Header)

    def test_h1_html(self):
        self.assertEqual(self.h1.html('Header 1'),'<h1>Header 1</h1>')

class HeaderTwoTest(unittest.TestCase):
    def setUp(self):
        self.h2 = tags.Header(2)

    def test_h2_instantiation(self):
        self.assertEqual(self.h2.__class__,tags.Header)

    def test_h2_html(self):
        self.assertEqual(self.h2.html('Header 2'),'<h2>Header 2</h2>')

class HeaderThreeTest(unittest.TestCase):
    def setUp(self):
        self.h3 = tags.Header(3)

    def test_h3_instantiation(self):
        self.assertEqual(self.h3.__class__,tags.Header)

    def test_h3_html(self):
        self.assertEqual(self.h3.html('Header 3'),'<h3>Header 3</h3>')

class HeaderFourTest(unittest.TestCase):
    def setUp(self):
        self.h4 = tags.Header(4)

    def test_h4_instantiation(self):
        self.assertEqual(self.h4.__class__,tags.Header)

    def test_h4_html(self):
        self.assertEqual(self.h4.html('Header 4'),'<h4>Header 4</h4>')

class HeaderFiveTest(unittest.TestCase):
    def setUp(self):
        self.h5 = tags.Header(5)

    def test_h5_instantiation(self):
        self.assertEqual(self.h5.__class__,tags.Header)

    def test_h5_html(self):
        self.assertEqual(self.h5.html('Header 5'),'<h5>Header 5</h5>')

class HeaderSixTest(unittest.TestCase):
    def setUp(self):
        self.h6 = tags.Header(6)

    def test_h6_instantiation(self):
        self.assertEqual(self.h6.__class__,tags.Header)

    def test_h6_html(self):
        self.assertEqual(self.h6.html('Header 6'),'<h6>Header 6</h6>')

class StyleTest(unittest.TestCase):
    def setUp(self):
        self.style = tags.Style({'type':'application/stylesheet'})

    def test_style_instantiation(self):
        self.assertEqual(self.style.__class__,tags.Style)
        
    def test_style_html(self):
        self.assertEqual(self.style.html('.wrapper { margin:0; }'),'<style type="application/stylesheet">.wrapper { margin:0; }</style>')

class SectionTest(unittest.TestCase):
    def setUp(self):
        self.section = tags.Section({'class':'articles-stack'})

    def test_section_instantiation(self):
        self.assertEqual(self.section.__class__,tags.Section)

    def test_section_html(self):
        self.assertEqual(self.section.html('Insert your article on that tag'),'<section class="articles-stack">Insert your article on that tag</section>')

class OrderedListTest(unittest.TestCase):
    def setUp(self):
        self.ordered_list = tags.OrderedList({'class':'contacts-list'})

    def test_ordered_list_instantiation(self):
        self.assertEqual(self.ordered_list.__class__,tags.OrderedList)

    def test_ordered_list_html(self):
        self.assertEqual(self.ordered_list.html('List items comes here'),'<ol class="contacts-list">List items comes here</ol>')

class UnorderedListTest(unittest.TestCase):
    def setUp(self):
        self.unordered_list = tags.UnorderedList({'class':'clients-list'})

    def test_unordered_list_instantiation(self):
        self.assertEqual(self.unordered_list.__class__,tags.UnorderedList)

    def test_unordered_list_html(self):
        self.assertEqual(self.unordered_list.html('List items comes here'),'<ul class="clients-list">List items comes here</ul>')

class ListItemTest(unittest.TestCase):
    def setUp(self):
        self.list_item = tags.ListItem({'class':'client'})

    def test_list_item_instantiation(self):
        self.assertEqual(self.list_item.__class__,tags.ListItem)

    def test_list_item_html(self):
        self.assertEqual(self.list_item.html('John Doe'),'<li class="client">John Doe</li>')

class TableTest(unittest.TestCase):
    def setUp(self):
        self.table = tags.Table({'class':'table-test-component'})

    def test_table_item_instantiation(self):
        self.assertEqual(self.table.__class__,tags.Table)

    def test_table_html(self):
        self.assertEqual(self.table.html('Table Content'),'<table class="table-test-component">Table Content</table>')

class TableHeadTest(unittest.TestCase):
    def setUp(self):
        self.table_head = tags.TableHead({'class':'table-test-component'})

    def test_table_head_instantiation(self):
        self.assertEqual(self.table_head.__class__,tags.TableHead)

    def test_table_head_html(self):
        self.assertEqual(self.table_head.html('Table Head Content'),'<thead class="table-test-component">Table Head Content</thead>')

class ListItemTest(unittest.TestCase):
    def setUp(self):
        self.list_item = tags.ListItem({'class':'client'})

    def test_list_item_instantiation(self):
        self.assertEqual(self.list_item.__class__,tags.ListItem)

    def test_list_item_html(self):
        self.assertEqual(self.list_item.html('John Doe'),'<li class="client">John Doe</li>')

class TableHeadTest(unittest.TestCase):
    def setUp(self):
        self.table_head = tags.TableHead()

    def test_table_head_instantiation(self):
        self.assertEqual(self.table_head.__class__,tags.TableHead)

    def test_table_head_html(self):
        self.assertEqual(self.table_head.html('Table Head Content'),'<thead>Table Head Content</thead>')

class TableBodyTest(unittest.TestCase):
    def setUp(self):
        self.table_body = tags.TableBody({'class':'table-body-stripped'})

    def test_table_body_instantiation(self):
        self.assertEqual(self.table_body.__class__,tags.TableBody)

    def test_table_body_html(self):
        self.assertEqual(self.table_body.html('Table Body Content'),'<tbody class="table-body-stripped">Table Body Content</tbody>')

class TableRowTest(unittest.TestCase):
    def setUp(self):
        self.table_row = tags.TableRow({'class':'even'})

    def test_table_row_instantiation(self):
        self.assertEqual(self.table_row.__class__,tags.TableRow)

    def test_table_row_html(self):
        self.assertEqual(self.table_row.html('Table Row Content'),'<tr class="even">Table Row Content</tr>')

class TableDimmerTest(unittest.TestCase):
    def setUp(self):
        self.table_dimmer = tags.TableDimmer({'class':'odd'})

    def test_table_dimmer_instantiation(self):
        self.assertEqual(self.table_dimmer.__class__,tags.TableDimmer)

    def test_table_dimmer_html(self):
        self.assertEqual(self.table_dimmer.html('Table Dimmer Content'),'<td class="odd">Table Dimmer Content</td>')

class IframeTest(unittest.TestCase):
    def setUp(self):
        self.iframe = tags.Iframe({'src':'sample.html'})

    def test_iframe_instantiation(self):
        self.assertEqual(self.iframe.__class__,tags.Iframe)

    def test_iframe_html(self):
        self.assertEqual(self.iframe.html('Iframe content'),'<iframe src="sample.html">Iframe content</iframe>')

if __name__ == '__main__':
    unittest.main(verbosity=2)
