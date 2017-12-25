from six import wraps
import logging
import time
import hermes.backend.redis
import hermes.backend.dict

logger = logging.getLogger('FunctionOptimizer')
hermescache = hermes.Hermes(hermes.backend.dict.Backend)
# hermescache = hermes.Hermes(hermes.backend.redis.Backend, ttl = 600, host = 'localhost', db = 1)

from numba import jit as numba_jit


def optimizer(cache_type=None,cache_config={},jit_type=None,jit_config={},profile_type=None,profile_config={}):
	def optimizer_decorator(func):
		decorated_func = func

		###########################  jit Optimisation  #################################
		if jit_type and jit_type.lower() == "numba":
			decorated_func = numba_jit(**jit_config)(decorated_func)
		
		###########################  Cache Optimisation  #################################
		if cache_type and cache_type.lower() == "hermes":
			decorated_func = hermescache(**cache_config)(decorated_func)	
			decorated_func.__defaults__ = func.__defaults__				# Hermes omits __defaults__ in resulting Cached fn object

		########################### Optimisation Profiling #################################
		if profile_type and profile_type.lower() == "time":
			def timeProfile_decorater(infunc):	
				def timeProfiler(*args,**kwargs):
					start_time = time.time()
					return_val = infunc(*args, **kwargs)
					end_time = time.time()
					logger.info("{} : Excecution wall time : {}".format(func.__name__,(end_time-start_time)))
					return return_val
				return timeProfiler  
			decorated_func = timeProfile_decorater(decorated_func)
				
		if decorated_func != func:
			decorated_func = wraps(func)(decorated_func)
		return decorated_func
	return optimizer_decorator

if __name__ == '__main__':		
	logging.basicConfig(level=logging.INFO)
	@optimizer(cache_type="hermes",cache_config={"tags":('tag1', 'tag2')}, jit_type='numba',jit_config={'nopython':True},profile_type='time')
	def get_one(name):
		return name+1*8.9/3-37987

	print(get_one(2))
	print(get_one(2))
	print(get_one(3))
	print(get_one(2))
	print(get_one(3))
	print(get_one(2))
	print(get_one(3))
	