from websocket_server import WebsocketServer


def new_client(client, server):
    print("New client connected and was given id %d" % client['id'])
    server.send_message_to_all("Hey all, a new client has joined us")


PORT = 9001
server = WebsocketServer(PORT, "0.0.0.0")
server.set_fn_new_client(new_client)
# server.set_fn_client_left(client_left)
# server.set_fn_message_received(message_received)
server.run_forever()
