import socket

host = "hw1.alexbers.com"
my_cookie = "user=877aa9ebd0f3f72d673a37c67d00556c"

request = (
    "GET / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    f"Cookie: {my_cookie}\r\n"
    "Connection: close\r\n"
    "\r\n"
).encode("ascii")

s = socket.create_connection((host, 80), timeout=10)
s.sendall(request)

response_bytes = b""

while True:
    resp = s.recv(4096)
    if not resp:
        break
    response_bytes += resp

s.close()

response_text = response_bytes.decode("utf-8", errors="ignore")
print(response_text)