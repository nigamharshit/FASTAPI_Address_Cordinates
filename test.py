import requests

# response = requests.get('http://127.0.0.1:8000/retrieve_all_address_details')

# json_output = response.json()

# print(json_output)
# print()
# print(type(json_output))
# print()
# for i in json_output:
#     print(i.get('lattitude'))


# response = requests.delete('http://127.0.0.1:8000/delete_address_by_id',params={'sl_id' : 0})
# print(response)
# print(response.text)
# print(response.content)
# print(response.headers)


response = requests.post('http://127.0.0.1:8000/address_within_distance',params={'address' : 'Railway Station Prayagraj India', 'distance': 10})
print(response)
print(response.text)
print(response.content)
print(response.headers)
