from gpsrecv.reader import Serial
import re
import time
import datetime
import urllib.request
import urllib.parse
import traceback
from queue import Queue

GPRMC_RE = re.compile("^\$GPRMC,(\d+\.\d+),([AV]),(\d+\.\d+|),([NS]|),(\d+\.\d+|),([EW]|),(\d+\.\d+|),(\d+\.\d+|),(\d{6}),([^,]*),([^,]*),([NADE])\*")


ADD_WAYPOINT_URL = "http://localhost:8000/trasponder/waypoint/"



def main(port, name, url):
    queue = Queue(20)

    reader = Serial(port, name=name, queue=queue)
    reader.start()

    while True:
        item = queue.get()
        m = GPRMC_RE.match(item["data"])

        try:
            if m:
                parsed = m.groups()

                print(item["data"])
                print(parsed)

                data = {
                        "transponder":item["sender"],
                        "created":datetime.datetime.strptime("{0} {1}".format(parsed[0].split(".")[0], parsed[8]), "%H%M%S %d%m%y") + datetime.timedelta(hours=9),
                        "latitude":parsed[2],
                        "longitude":parsed[4],
                        }

                print(data)

                post_data = urllib.parse.urlencode(data).encode(encoding='utf-8')
                with urllib.request.urlopen(url=url, data=post_data) as response:
                    body = response.read()
                    print(response.info())
                    print(body)

        except:
            traceback.print_exc()

if __name__ == "__main__":
    import sys

    port = sys.argv[1]
    name = sys.argv[2]
    url = ADD_WAYPOINT_URL
    if len(sys.argv) > 3:
        url = sys.argv[3]

    print("Port: {0}".format(port))
    print("Name: {0}".format(name))
    print(" URL: {0}".format(url))

    main(port, name, url)
