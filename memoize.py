class memoize:
	def __init__ (self, func, cache=None, debug=0, name=None):
		self.func = func
		if cache is None:
			cache  = {}
		self.cache = cache
		self.proto = dict (cache)
		self.debug = debug
		if name is None:
			name = func.__name__
		self.name = name

	def __call__ (self, *args, **kwargs):
		params = args + tuple (kwargs.items ())
		i = len (args)
		if params not in self.cache:
			if self.debug:
				print ("+", *(args + (kwargs,)))
			self.cache [params] = self.func (self, *args, **kwargs)
			i += 1
		if self.debug > 1:
			print (' ', *(args + (kwargs,)))
		return self.cache [params]

	def reset (self):
		self.cache.clear ()
		self.cache.update (self.proto)

class recurse:
	def __init__ (self, func, debug=0):
		self.func = func
		self.debug=debug

	def __call__ (self, *args, **kwargs):
		if sedebug: print (*args, **kwargs)
		return self.func (self, *args, **kwargs)

core = lambda self, n: self (n-1) + self (n-2) if n > 1 else n
fib = memoize (core)
raw = recurse (core)

def timefunc (func, *args, **kwargs):
	import time
	t = time.clock()
	x = func (*args, **kwargs)
	print (x)
	return (time.clock() - t)

def comp (n, func=fib):
	func.reset()
	#a = timefunc (raw, n)
	b = timefunc (func, n)
	c = timefunc (func, n)
	print ('Speed for f of', func.__name__)
	print ('=========================')
	print ('Operations per second:\n')
	#print ('uncached:', 1//a)
	print ('cached:', 1//b)
	print ('fully cached:', 1//c)
	print ('=========================')
	#print ('cached is', a//b, 'times faster than uncached')
	print ('fully cached is', b//c, 'times faster than cached')
	#print ('fully cached is', a//c, 'times faster than uncached')
