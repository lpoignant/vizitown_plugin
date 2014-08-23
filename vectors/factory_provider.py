from vector import Vector


class VectorFactory:

	def __init__(self):
		print "Nothing"

	def create_provider(self, QgsMapLayer):
		vector = Vector(QgsMapLayer)