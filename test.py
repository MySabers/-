import requests
import ujson
import time


class Source:
    def __init__(self, _conf):
        self.conf = _conf
        self.url_header = self.conf["header"]
        self.url = self.conf["url"]
    def get_data(self):
        while 1:
            try:
                response = requests.get(self.url, headers=self.url_header,timeout=1)
                time.sleep(1)
            except Exception as e:
                print(e)
            if response.content:
                # content = bytes.decode(response.content)
                content = response.content
            yield content

if __name__ == "__main__":
    config = {
      "url": "http://10.255.175.187:8001/datahub/pull?size=50&type=asset&sub=sa_storage",
      "method": "GET",
      "header": {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"},
      "body": ""
    }
    source = Source(config)

    for s in source.get_data():
        items = ujson.loads(str(s, "utf-8"))["items"]
        for item in items:
            try:
                i = item["os"]
            except Exception:
                print (item)

