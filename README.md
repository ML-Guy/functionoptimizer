# functionoptimizer
Optimization library for functions. It aggregates available optimisations tools like numba jit, function caching etc.

## Features:
 - [x] Numba JIT
 - [x] Function caching
    - [x] Dict based - hermes backend
    - [x] Redis based - hermes backend
    - [ ] disk caching - Diskcache backend
 - [ ] parallelization support
 - [x] Profiling
   - [x] Time
   - [ ] Code/lineprofiler
   - [ ] cprofiler
   - [ ] memory profiler
 - [ ] Debug
   - [ ] pdb
   - [ ] Exception pdb

# Requirement
- sudo apt-get install mercurial
- redis
