import json
import urllib.request

get_data_url = "https://opentdb.com/api.php?amount=10&category=18&type=boolean"
res = urllib.request.urlopen(get_data_url)
res_body = res.read()

data = json.loads(res_body.decode("utf-8"))
question_data = data["results"]
