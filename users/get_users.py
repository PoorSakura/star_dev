import json
import time

with open("./users.json", encoding='utf-8') as f:
    content = f.read()
    a = json.loads(content)
    c = {}
    size = 0
    gte_50 = 0
    for v in a["results"]:
        time.sleep(1)
        size += v["home_storage_in_gb"]
        if v["home_storage_in_gb"] >= 100:
            gte_50 += 1
        if v["create_user"] not in c:
            c[v["create_user"]] = True
    print(len(c))
    print(size)
    print(gte_50)

