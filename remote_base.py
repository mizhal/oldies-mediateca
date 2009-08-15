import rpc_client

class RemoteBase:
        def __init__(self, host, port):
                self.rpc = rpc_client.MediatecaClient(host, port)
                
        def ls(self):
                l = self.rpc.playlistLength()
                all = []
                base = 0
                if l % 10 == 0:
                        els = l/10
                else:
                        els = l/10 +1
                for i in range(els):
                        all.extend(self.rpc.playlist(base, base+10)) 
                        base += 10
                        
                for i, name in enumerate(all):
                        print i, ":", name