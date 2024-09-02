class Pagination:
	def __init__(self, ranges, include_pages=None, exclude_pages=None, booklet=None) -> None:
		self.arr = []
		self.book = []
		self.ranges = ranges
		self.nro_pages = booklet
		self.inp = include_pages
		self.exp = exclude_pages if exclude_pages is not None else []

	def process(self, nro):
		if len(self.ranges) == 0:
			self.ranges = [(1, nro)]

		for r in self.ranges:
			self.book.extend(list(range(r[0], r[1] + 1)))

		if self.inp is not None:
			self.book.extend(self.inp)

		self.book = list(set(self.book))
		self.book.sort()

		for p in self.exp:
			if p in self.book:
				self.book.remove(p)

	def make_separation(self):
		""" Si se usa la separacion por encuadenacion
			Entonces se verifica que exista y se itera en el
		"""
		nro = len(self.book)
		nro4 = nro if nro % 4 == 0 else nro + 4 - (nro % 4)
		if self.nro_pages is None:
			self.nro_pages = int(nro4 / 4)

		for i in range(0, nro4, self.nro_pages * 4):
			end = min(i + self.nro_pages * 4 - 1, nro4 - 1)
			self.make_pagination(i, end)

	def make_pagination(self, ini=0, end=0):
		""" Con los valores ini = 0 y end = 40
			recorre el arreglo 10 veces con los valores [0, 2, 4,..., 18]
		"""
		for i in range(0, int((end - ini) / 2), 2):
			self.arr.append((self.gb(ini + i), self.gb(end - i), self.gb(ini + i + 1), self.gb(end - i - 1)))

	def gb(self, ind):
		return self.book[ind] - 1 if ind < len(self.book) else None
