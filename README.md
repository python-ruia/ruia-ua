## ruia-ua

simple user-agent middleware for [ruia](https://github.com/howie6879/ruia)

```text
Notice:  Works on ruia >= 0.0.1
```

### Installation

```shell
pip install ruia-ua
```

### Usage

`ruia-ua` will be automatically populated with a random `User-Agent` for your request's `headers`

```python
from ruia import AttrField, TextField, Item, Spider
from ruia import middleware


class HackerNewsItem(Item):
    target_item = TextField(css_select='tr.athing')
    title = TextField(css_select='a.storylink')
    url = AttrField(css_select='a.storylink', attr='href')

    async def clean_title(self, value):
        return value


class HackerNewsSpider(Spider):
    start_urls = ['https://news.ycombinator.com/news?p=1', 'https://news.ycombinator.com/news?p=2']
    concurrency = 10

    async def parse(self, res):
        items = await HackerNewsItem.get_items(html=res.html)
        for item in items:
            print(item.title)


if __name__ == '__main__':
    HackerNewsSpider.start(middleware=middleware)
```

Enjoy it :)