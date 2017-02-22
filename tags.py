'''Tags'''
from string import Template

SP = ' '
INTROSPECTIVE_KEYS = ('value','html')

def assertion_tag_error(tag, content=''):
    message = content or 'You must be insert correct parameters, because the (%s) was unexpected'
    if content and tag:
        return message % (tag.html())
    return message % tag.html()

class NFZ():
    def __init__(self):
        self.UTF_WITHOUT_VALUE = Template('<$tname $tattrs_fslash>')
        self.CTF = Template('<$tname $tattrs>$tvalue</$tname>')
        self.CTF_WITHOUT_ATTRS = Template('<$tname>$tvalue</$tname>')
#nfz = NFZ()
#assert nfz.UTF_WITHOUT_VALUE.template == '<$tname $tattrs_fslash>', 'Unexpected tag representation without value'
#assert nfz.CTF.template == '<$tname $tattrs>$tvalue</$tname>', 'Unexpected tag representation with value'
#assert nfz.CTF_WITHOUT_ATTRS.template == '<$tname>$tvalue</$tname>', 'Unexpected tag representation without attrs'

class Attbs():
    def __init__(self,attrs={}):
        self.__attrs__ = attrs
        self.attrs = attrs.keys()

    def select_by(self,attrs={},pass_those_keys=INTROSPECTIVE_KEYS):
        out = {}
        for (k,v) in attrs.items():
            if k not in pass_those_keys:
                out[k]=v
        return out

    def expose(self,order=True):
        out = []
        attrs = self.select_by(self.__attrs__)
        for (k,v) in attrs.items():
            if v:
                out.append('%s="%s"' % (k,v))
            else:
                out.append('%s' % (k))
        if order: out.sort()
        return out

    def join(self):
        return SP.join(self.expose()).strip()

class Tag():
    def __init__(self,attrs={},name='',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

    def html(self,value=''):
        tag = {}
        attbs = Attbs(self.attrs)
        exposed_attrs = attbs.expose()
        transformed_attrs = attbs.join()
        nfz = NFZ()
        is_unclosed_with_transformed_attrs = not self.closed and transformed_attrs
        is_closed_with_untransformed_attrs = self.closed and not transformed_attrs
        if is_unclosed_with_transformed_attrs:
            return nfz.UTF_WITHOUT_VALUE.substitute({'tname':self.name,'tattrs_fslash':'%s%s' % (transformed_attrs,(self.slash and '/' or ''))})
        elif is_closed_with_untransformed_attrs:
            return nfz.CTF_WITHOUT_ATTRS.substitute({'tname':self.name,'tvalue':value})
        else:
            return nfz.CTF.substitute({'tname':self.name,'tattrs':transformed_attrs,'tvalue':value})

#p = Tag({'class':'message'},'p')
#assert p.html('Hello from taggler') == '<p class="message">Hello from taggler</p>', assertion_tag_error(p)

class Div(Tag):
    def __init__(self,attrs={},name='div',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#div = Div({'class':'holder'})
#assert div.html('Div model') == '<div class="holder">Div model</div>', assertion_tag_error(div)

class Image(Tag):
    def __init__(self,attrs={},name='img',closed=False,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#img = Image({'class':'outer-figure-holder','src':'//placehold.it/50x50/'})
#assert img.html() == '<img class="outer-figure-holder" src="//placehold.it/50x50/"/>', assertion_tag_error(img)

class Span(Tag):
    def __init__(self,attrs={},name='span',closed=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed

#span = Span({'class':'text-holding'})
#assert span.html('Peace into the heart') == '<span class="text-holding">Peace into the heart</span>', assertion_tag_error(span)

class Anchor(Tag):
    def __init__(self,attrs={},name='a',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#a = Anchor({'class':'anchor-point','href':'//kaiquesilva.com.br'})
#assert a.html('Anchor value') == '<a class="anchor-point" href="//kaiquesilva.com.br">Anchor value</a>', assertion_tag_error(a)

class Abbr(Tag):
    def __init__(self,attrs={},name='abbr',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#abbr = Abbr({'title':'Feel The Hacking'})
#assert abbr.html('FTH') == '<abbr title="Feel The Hacking">FTH</abbr>', assertion_tag_error(abbr)

class Address(Tag):
    def __init__(self,attrs={},name='address',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#address = Address()
#assert address.html('Av. Dr. Ministro Xavier, 0') == '<address>Av. Dr. Ministro Xavier, 0</address>', assertion_tag_error(address)

class Area(Tag):
    def __init__(self,attrs={},name='area',closed=False,slash=False):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#area = Area({'shape':'rect','coords':'0,0,82,126','href':'sun.html','alt':'Sun'})
#assert area.html() == '<area alt="Sun" coords="0,0,82,126" href="sun.html" shape="rect">', assertion_tag_error(area)

class Article(Tag):
    def __init__(self,attrs={},name='article',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#article = Article()
#assert article.html('Text inside of the article tag') == '<article>Text inside of the article tag</article>', assertion_tag_error(article)

class Aside(Tag):
    def __init__(self,attrs={},name='aside',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#aside = Aside()
#assert aside.html('Text inside of aside tag') == '<aside>Text inside of aside tag</aside>', assertion_tag_error(aside)

class Audio(Tag):
    def __init__(self,attrs={},name='audio',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#audio = Audio({'controls':''})
#assert audio.html('Text inside of audio tag') == '<audio controls>Text inside of audio tag</audio>', assertion_tag_error(audio)

class Source(Tag):
    def __init__(self,attrs={},name='source',closed=False,slash=False):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#source = Source({'src':'horse.ogg','type':'audio/ogg'})
#assert source.html() == '<source src="horse.ogg" type="audio/ogg">', assertion_tag_error(source)

class Bold(Tag):
    def __init__(self,attrs={},name='b',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#bold = Bold()
#assert bold.html('this is a bold text') == '<b>this is a bold text</b>', assertion_tag_error(bold)

class Paragraph(Tag):
    def __init__(self,attrs={},name='p',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#paragraph = Paragraph()
#assert paragraph.html('this is a p tag') == '<p>this is a p tag</p>', assertion_tag_error(paragraph)

class Base(Tag):
    def __init__(self,attrs={},name='base',closed=False,slash=False):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#base = Base({'href':'http://kaiquesilva.com.br/resources/','target':'_blank'})
#assert base.html() == '<base href="http://kaiquesilva.com.br/resources/" target="_blank">', assertion_tag_error(base)

class Body(Tag):
    def __init__(self,attrs={},name='body',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#body = Body()
#assert body.html() == '<body></body>', assertion_tag_error(body)

class Head(Tag):
    def __init__(self,attrs={},name='head',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#head = Head()
#assert head.html() == '<head></head>', assertion_tag_error(head)

class Link(Tag):
    def __init__(self,attrs={},name='link',closed=False,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#link = Link({'href':'style.css','type':'application/stylesheet'})
#assert link.html() == '<link href="style.css" type="application/stylesheet"/>', assertion_tag_error(link)

class Script(Tag):
    def __init__(self,attrs={},name='script',closed=False,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#script = Script({'src':'main.js'})
#assert script.html() == '<script src="main.js"/>', assertion_tag_error(script)

class Meta(Tag):
    def __init__(self,attrs={},name='meta',closed=False,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#meta = Meta({'name':'robots','content':'NONE,NOARCHIVE'})
#assert meta.html() == '<meta content="NONE,NOARCHIVE" name="robots"/>', assertion_tag_error(meta)

class Header(Tag):
    def __init__(self,n=1,attrs={},name='h%s',closed=True,slash=True):
        self.n = n
        self.name = name % (n)
        self.attrs = attrs
        self.closed = closed
        self.slash = slash

#h1 = Header(1)
#assert h1.html('Header 1') == '<h1>Header 1</h1>', assertion_tag_error(h1)
#h2 = Header(2)
#assert h2.html('Header 2') == '<h2>Header 2</h2>', assertion_tag_error(h2)
#h3 = Header(3)
#assert h3.html('Header 3') == '<h3>Header 3</h3>', assertion_tag_error(h3)
#h4 = Header(4)
#assert h4.html('Header 4') == '<h4>Header 4</h4>', assertion_tag_error(h4)
#h5 = Header(5)
#assert h5.html('Header 5') == '<h5>Header 5</h5>', assertion_tag_error(h5)
#h6 = Header(6)
#assert h6.html('Header 6') == '<h6>Header 6</h6>', assertion_tag_error(h6)

class Style(Tag):
    def __init__(self,attrs={},name='style',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash
#style = Style({'type':'application/stylesheet'})
#assert style.html('.wrapper { margin:0; }') == '<style type="application/stylesheet">.wrapper { margin:0; }</style>', assertion_tag_error(style)

class Section(Tag):
    def __init__(self,attrs={},name='section',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash
#section = Section({'class':'articles-stack'})
#assert section.html('Here you insert your article') == '<section class="articles-stack">Here you insert your article</section>', assertion_tag_error(section)

class OrderedList(Tag):
    def __init__(self,attrs={},name='ol',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash
#ol = OrderedList({'class':'contacts-list'})
#assert ol.html('List items comes here') == '<ol class="contacts-list">List items comes here</ol>', assertion_tag_error(ol)

class UnorderedList(Tag):
    def __init__(self,attrs={},name='ul',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash
#ul = UnorderedList({'class':'clients-list'})
#assert ul.html('List items comes here') == '<ul class="clients-list">List items comes here</ul>', assertion_tag_error(ul)

class ListItem(Tag):
    def __init__(self,attrs={},name='li',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash
#li = ListItem({'class':'client'})
#assert li.html('John Doe') == '<li class="client">John Doe</li>', assertion_tag_error(li)

class Table(Tag):
    def __init__(self,attrs={},name='table',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash
#table = Table({'class':'elements'})
#assert table.html('Table of Contents') == '<table class="elements">Table of Contents</table>', assertion_tag_error(table)

class TableHead(Tag):
    def __init__(self,attrs={},name='thead',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = closed
#thead = TableHead()
#assert thead.html('Table Head Content') == '<thead>Table Head Content</thead>', assertion_tag_error(thead)

class TableBody(Tag):
    def __init__(self,attrs={},name='tbody',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash
#tbody = TableBody({'class':'table-body-stripped'})
#assert tbody.html('Table Body Content') == '<tbody class="table-body-stripped">Table Body Content</tbody>', assertion_tag_error(tbody)

class TableRow(Tag):
    def __init__(self,attrs={},name='tr',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash
tr = TableRow({'class':'even'})
assert tr.html('Table Row Content') == '<tr class="even">Table Row Content</tr>', assertion_tag_error(tr)

class TableDimmer(Tag):
    def __init__(self,attrs={},name='td',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash
td = TableDimmer({'class':'odd'})
assert td.html('Table Dimmer Content') == '<td class="odd">Table Dimmer Content</td>', assertion_tag_error(td)

class Iframe(Tag):
    def __init__(self,attrs={},name='iframe',closed=True,slash=True):
        self.name = name
        self.attrs = attrs
        self.closed = closed
        self.slash = slash
iframe = Iframe({'src':'sample.html'})
assert iframe.html('Iframe content') == '<iframe src="sample.html">Iframe content</iframe>', assertion_tag_error(iframe)
