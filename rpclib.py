##
# Funcion rpcmap
#
# genera un decorador vinculado a un diccionario,
# de tal manera que todas las llamadas a @rpc(N)
# registran la funcion que viene despues en el
# diccionario de operaciones

def rpcmap(operation_map):
	
	def rpc(id):
		def bind(method):
			operation_map[id] = method
			return method
		
		return bind
	
	return rpc
	
class ExampleRPC:
	operations = {}
	
	rpc = rpcmap(operations)
	
	@rpc(1)
	def op1(self, data):
		pass
		
	@rpc(2)
	def op2(self, data):
		pass