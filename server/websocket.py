from websocket_server import WebsocketServer


def new_client(client, server):
    print("New client connected and was given id %d" % client['id'])
    server.send_message_to_all("Hey all, a new client has joined us")


def message_received(client, server, message):
    print("ClientNo(%d) said: %s" % (client['id'], message))
    # print(WebsocketServer.clients)
    if (len(WebsocketServer.clients) >= 2):
        server.send_message(WebsocketServer.clients[1], message)


def client_left(client, server):
    print('ClientNo(%d) left' % client['id'])


PORT = 9001
server = WebsocketServer(PORT, '0.0.0.0')
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.set_fn_client_left(client_left)
server.run_forever()
