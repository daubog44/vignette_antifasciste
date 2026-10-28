"""Verifica immagini, miniature e ordine delle opere nella pagina generata."""
import json
import html
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
import unittest

import content
from prot import PROT

ROOT = Path(__file__).resolve().parent.parent


class Figures(HTMLParser):
    def __init__(self, page):
        super().__init__()
        self.images = []
        self.indices = []
        self.feed(page)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'figure':
            self.indices.append(int(attrs['data-i']))
        if tag == 'img' and attrs.get('src'):
            self.images.append(attrs)


class BuildTest(unittest.TestCase):
    def test_images_and_carousel(self):
        subprocess.run([sys.executable, str(ROOT / 'sorgenti/build.py')], check=True)
        page = (ROOT / 'index.html').read_text(encoding='utf-8')
        figures = Figures(page)
        data = json.loads(page.split('<script>var BASE=', 1)[1].split(';</script>', 1)[0])
        expected = []
        for chapter in content.CHAPTERS:
            for figure in chapter['figs']:
                expected.append(figure[1])
                expected.extend(p['title'] for p in PROT if p['after'] == figure[0])
        self.assertEqual(len(data), sum(len(c['figs']) for c in content.CHAPTERS) + len(PROT))
        self.assertEqual([item['t'] for item in data], expected)
        self.assertEqual(figures.indices, list(range(len(expected))))
        self.assertEqual(len(figures.images), len(expected))
        self.assertEqual(len({item['s'] for item in data}), len(expected))
        assets = json.loads((ROOT / 'sorgenti/immagini.json').read_text())
        self.assertEqual(set(assets), {p['key'] for p in PROT})
        for work in PROT:
            self.assertIn(html.escape(work['link'], quote=True), page)
            self.assertTrue(all(work[k] for k in ('d', 'i', 's', 'a')))
            self.assertTrue(all(assets[work['key']][k] for k in ('page', 'rights', 'verification')))
        for image, item in zip(figures.images, data):
            with self.subTest(image=item['s']):
                self.assertEqual(image['src'], item['s'])
                self.assertTrue(image['alt'])
                self.assertEqual((int(image['width']), int(image['height'])), (item['w'], item['h']))
                for key in ('s', 'th'):
                    self.assertTrue((ROOT / item[key]).is_file(), item[key])
        self.assertIn(f'Numero unico · {len(expected)} immagini', page)
        self.assertNotIn('Guardala qui', page)
        self.assertNotIn('data-local=', page)
        self.assertNotIn("location.protocol==='file:'", page)


if __name__ == '__main__':
    unittest.main()
