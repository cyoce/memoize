def normal (n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		print ("+", n)
		return normal (n - 1) + normal (n - 2)

def cached (n, depth=0, cache={0:0, 1:1}):
	if n not in cache:
		print ("+", n)
		cache[n] = cached (n - 1, depth + 1) + cached (n - 2, depth + 1)
	result = cache[n]
	if not depth:
		cache.clear ()
		cache.update ({0:0, 1:1})
	return result
