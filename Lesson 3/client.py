import test_chat
import jim

if __name__ == '__main__':
    client_name = input('Введите имя: ')

    parser = test_chat.create_parser()
    namespace = parser.parse_args()

    sock = test_chat.get_client_socket(namespace.addr, namespace.port)

    serv_addr = sock.getpeername()
    print(f'Connected to server: {serv_addr[0]}:{serv_addr[1]}')

    jim.PRESENCE['user']['account_name'] = client_name
    test_chat.send_data(sock, jim.PRESENCE)

    while True:
        data = test_chat.get_data(sock)

        if data['response'] != '200':
            break

        msg = input('Введите сообщение ("exit" для выхода): ')
        jim.MESSAGE['message'] = msg
        test_chat.send_data(sock, jim.MESSAGE)

    sock.close()
