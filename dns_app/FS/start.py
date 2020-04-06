import requests
data={
    "hostname":"fibonacci.com",
    "ip":"127.0.0.1",
    "as_ip":"127.0.0.1",
    "as_port":"53533"
}
print(requests.put("http://127.0.0.1:9090/register",json=data).content)
