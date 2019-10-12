import json
data = {}
with open("input.json") as json_file:
	data = json.load(json_file)

if data:
	topthree = {}
	for result in sorted(data['server_stats'], key=lambda x: x['service']):
		if not result['service'] in topthree.keys():
			topthree[result['service']] = {}
		else:
			if not result['country'] in topthree[result['service']]:
				topthree[result['service']][result['country']] = result['events']
			else:
				topthree[result['service']][result['country']] += result['events']	

	for final_result, inner in topthree.items():
		inner = sorted(inner.items(), key=lambda j: int(j[1]), reverse=True)[:3]
		print(final_result)
		print(inner)

