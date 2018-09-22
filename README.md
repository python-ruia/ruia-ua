## aspider-ua

simple user-agent middleware for [aspider](https://github.com/howie6879/aspider)

```text
Notice:  Works on aspider >= 0.0.8
```

### Installation

```shell
pip install aspider-ua
```

### Usage

`aspider-ua` will be automatically populated with a random `User-Agent` for your request's `headers`

```python
from aspider import AttrField, TextField, Item, Spider
from aspider_ua import middleware


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