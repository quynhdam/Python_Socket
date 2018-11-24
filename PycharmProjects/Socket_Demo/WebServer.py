import socket
#khai báo địa chỉ Host và cổng kết nối
HOST = 'localhost'
PORT = 8888
#khai báo và khởi tạo socket
#thiết lập điạ chỉ kết nối: AddressFamily = socket.AF_inet(thiết lập dưới dạng IPv4)
#                                           socket.AF_6 - thiết lập dưới dạng IPv6 và AF_UNIX
#thiết lập giao thức truyền tin cho socket: socketType = socket.SOCK_STREAM(TCP) hoặc socket_SOCK_DGRAM(UDP)
#thiết lập loại giao thức Protocol: có thể k cần thiết lập, mặc định bằng 0,
# trong ví dụ này nó k được thiết lập và mặc định bằng 0

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
# lắng nghe đến địa chỉ address và port(bind(add, port)
listen_socket.bind((HOST, PORT))
#thiết lập mở kết nối trên server
#  với tham số truyền vào là số kết nối được phép (nhỏ nhất là 0 và lớn nhất là do cấu hình của server).
listen_socket.listen(1)
print("Serving HTTP on port %s ..." %PORT)

# thiết lập chấp nhận một kết nối,
# và nó sẽ trả về một tuple gồm 2 thông số (conn, address) để chúng ta có thể gửi ngược về client.
(client_connection, client_address) = listen_socket.accept()
#nhận dữ liệu và đọc nội dung qua giao thức TCP.
request = client_connection.recv(1024)
#in ra nội dung nhận được
while True:
    if not request:
        exit()
    else:
        print(request)

        #"""http_response = """b\
        #HTTP/1.1 200 OK

        #Hello, World!
        #"""
        #gửi dữ liệu về client
        #new=input()
        client_connection.sendall(request)
        #client_connection.close()