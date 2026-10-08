"""Verify the generated documentation's local links and canonical metadata."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import json

root = Path(__file__).resolve().parents[1] / 'website/build/picklejs'
errors = set()
references = 0

class Links(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global references
        values = dict(attrs)
        for key in ('href', 'src'):
            value = values.get(key)
            if not value:
                continue
            url = urlparse(value)
            if url.scheme not in ('', 'http', 'https') or (url.netloc and url.netloc != 'picklejs.toli.me') or not url.path:
                continue
            references += 1
            path = unquote(url.path)
            target = root / path.lstrip('/') if path.startswith('/') else current.parent / path
            if not any(item.is_file() for item in (target, target.with_suffix('.html'), target / 'index.html')):
                errors.add((str(current.relative_to(root)), value))
        if tag == 'link' and values.get('rel') == 'canonical':
            if not values.get('href', '').startswith('https://picklejs.toli.me/'):
                errors.add((str(current.relative_to(root)), 'incorrect canonical URL'))

pages = sorted(root.rglob('*.html'))
assert pages, 'Build the site first.'
for current in pages:
    Links().feed(current.read_text())
assert (root / 'LICENSE.txt').read_bytes() == (root.parents[2] / 'LICENSE').read_bytes(), 'License was not preserved.'
print(json.dumps({'html_pages': len(pages), 'local_references': references, 'errors': sorted(errors)}, indent=2))
raise SystemExit(bool(errors))
