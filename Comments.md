   *  need to grab a lock and accumulate the values from all the thread local
   *  Returns the exact size of the map.  Note this is not as cheap as typical
   *  size() implementations because, for each AtomicHashArray in this AHM, we
   * "expr.classValue()".
   * (Also, in fact we never actually invoke the value_type
   * @return True if the inserted element is the only one in the list
   * @return True if the inserted element is the only one in the list
   * Accumulates time spent outside benchmark.
   * and calls func() on the removed elements in the order from tail to head.
   * and calls func() on the removed elements in the order from tail to head.
   * and calls func() on the removed elements in the order from tail to head.
   * Atomically insert t at the head of the list.
   * Atomically insert t at the head of the list.
   * booleanValue().  This method therefore converts "expr" to
   * calling func() on every element */
   * can reason about the ordering: elements inserted since the last call to
   * can reason about the ordering: elements inserted since the last call to
   * clear --
   * construct a bunch of value_type when we first start up: if you
   * Construct an AtomicBitSet; all bits are initially false.
   * constructed, and casting them to atomic objects (see cellKeyPtr).
   * constructor.)  This is in order to avoid needing to default
   * Convert a primitive type expression into a wrapped instance.  Each
   * Convert a wrapper class instance to a specified primitive equivalent.
   * Convert a wrapper class instance to its primitive equivalent.  Each
   * create --
   * element in our cells even though the cell object has not been
   * emplace --
   * emplace --
   * erase --
   * Example: if elements are inserted in the order 1-2-3, the callback is
   * Example: if elements are inserted in the order 1-2-3, the callback is
   * find --
   * find --
   * findAt --
   * func() is called for all elements in the list at the moment
   * func() is called for all elements in the list at the moment
   * have an expensive default constructor for the value type this can
   * If-conditions bypass the explicit on operator bool.
   * insert --
   * insert --
   * interface as possible.
   * into the data storage.
   * invoked 3-2-1.  If the callback moves elements onto a stack, popping off
   * invoked 3-2-1.  If the callback moves elements onto a stack, popping off
   * list is empty at some point after the last invocation.  This way callers
   * list is empty at some point after the last invocation.  This way callers
   * Mark all cells as empty.
   * Note that the operation is a read-modify-write operation due to the use
   * Note that the operation is a read-modify-write operation due to the use
   * Note that the operation is a read-modify-write operation due to the use
   * Note: list must be empty on destruction.
   * Note: we're bending the rules a little here accessing the key
   * noticeably speed construction time for an AHA.
   * of fetch_and or fetch_or.
   * of fetch_and.
   * of fetch_or.
   * previous value of the bit.
   * previous value of the bit.
   * Read bit idx.
   * Repeatedly pops element from head,
   * Repeatedly replaces the head with nullptr,
   * Replaces the head with nullptr,
   * Return the size of the bitset.
   * Returns false if the list was empty.
   * Returns the unique index that can be used for access directly
   * reverseSweep() is called.  Unlike sweep() it does not loop to ensure the
   * reverseSweep() is called.  Unlike sweep() it does not loop to ensure the
   * reverseSweep() will be provided in LIFO order.
   * reverseSweep() will be provided in LIFO order.
   * Same as test() with the default memory order.
   * Set bit idx to false, using the given memory order. Returns the
   * Set bit idx to the given value, using the given memory order. Returns
   * Set bit idx to true, using the given memory order. Returns the
   * Similar to sweep() but calls func() on elements in LIFO order.
   * Similar to sweep() but calls func() on elements in LIFO order.
   * size --
   * Stops when the list is empty.
   * Stops when the list is empty.
   * the previous value of the bit.
   * the stack will produce the original insertion order 1-2-3.
   * the stack will produce the original insertion order 1-2-3.
   * This is for use inside of if-conditions, used in BENCHMARK macros.
   * translated to "Wrapper.valueOf(expr)".
   * wrapper class has a "classValue()" method, such as intValue() or
   * wrapper class has a static valueOf factory method, so "expr" gets
   * Yes, this is an overload of set(), to keep as close to std::bitset's
   1. The origin of this source code must not be misrepresented; you must not
   1. The origin of this source code must not be misrepresented; you must not
   2. Altered source versions must be plainly marked as such, and must not be
   2. Altered source versions must be plainly marked as such, and must not be
   3. This notice may not be removed or altered from any source distribution.
   3. This notice may not be removed or altered from any source distribution.
   arising from the use of this software.
   arising from the use of this software.
   base64.cpp and base64.h
   base64.cpp and base64.h
   Copyright (C) 2004-2008 RenÃ© Nyffenegger
   Copyright (C) 2004-2008 RenÃ© Nyffenegger
   freely, subject to the following restrictions:
   freely, subject to the following restrictions:
   including commercial applications, and to alter it and redistribute it
   including commercial applications, and to alter it and redistribute it
   Permission is granted to anyone to use this software for any purpose,
   Permission is granted to anyone to use this software for any purpose,
   RenÃ© Nyffenegger rene.nyffenegger@adp-gmbh.ch
   RenÃ© Nyffenegger rene.nyffenegger@adp-gmbh.ch
   This source code is provided 'as-is', without any express or implied
   This source code is provided 'as-is', without any express or implied
   warranty. In no event will the author be held liable for any damages
   warranty. In no event will the author be held liable for any damages
  //       "A simple geometric model for elastic deformation" by [Chao et al.
  //       (triangles or tets) 
  //       2010], rotations defined at vertices affecting incident edges and
  //       [Liu et al.  2010] or "A simple geometric model for elastic
  //       Alexa 2007], rotations defined at vertices affecting incident edges,
  //       default
  //       deformation" by [Chao et al.  2010], rotations defined at elements
  //       for surfaces, elements for planar meshes and tets (not fully
  //       Modeling" by [Sorkine and Alexa 2007] presented in section 4.2 of or
  //       opposite edges
  //       supported)
  //     ARAP_ENERGY_TYPE_DEFAULT  Choose one automatically: spokes and rims
  //     ARAP_ENERGY_TYPE_ELEMENTS  "A local-global approach to mesh parameterization" by
  //     ARAP_ENERGY_TYPE_SPOKES  "As-rigid-as-possible Surface Modeling" by [Sorkine and
  //     ARAP_ENERGY_TYPE_SPOKES-AND-RIMS  Adapted version of "As-rigid-as-possible Surface
 (at your option) any later version.
 (at your option) any later version.
 *         50%             50%           0.19         0.05
 *         85%             85%           0.20         0.06
 *         90%             90%           0.23         0.08
 *         95%             95%           0.27         0.10
 *      (especially for small keys and values).
 *      (see findAt()).
 *      be reused with clear() and never move).
 *      capacity.
 *      multi-threaded environments).
 *     Andrew Gvozdev - initial API and implementation
 *     Load Factor   Mem Efficiency   usec/Insert   usec/Find
 *     QNX Software Systems - Initial API and implementation
 *    - Can generate unique, long-lived 32-bit references for efficient lookup
 *    - Efficient memory usage if initial capacity is not over estimated
 *    - Good fragmentation properties (only allocates in large slabs which can
 *    - High-performance (~2-4x tbb::concurrent_hash_map in heavily
 *    - Keys must be native int32 or int64, or explicitly converted.
 *    - Max size limit of ~18x initial size (dependent on max load factor).
 *    - Memory is not freed or reclaimed by erase.
 *    - Must be able to specify unique empty, locked, and erased keys
 *    - Performance degrades linearly as size grows beyond initialization
 *   AHArray is a fixed size contiguous block of value_type cells.  When
 *   AHMap is a wrapper around AHArray sub-maps that allows growth and provides
 *   all copies or substantial portions of the Software.
 *   all copies or substantial portions of the Software.
 *   all copies or substantial portions of the Software.
 *   Also sets ret.index to the index of the key.  If the map is full, sets
 *   an interface closer to the STL UnorderedAssociativeContainer concept. These
 *   authors or copyright holders be liable for any claim, damages or other
 *   authors or copyright holders be liable for any claim, damages or other
 *   authors or copyright holders be liable for any claim, damages or other
 *   Benchmark performance with 8 simultaneous threads processing 1 million
 *   bytes.
 *   Christian R <c@ethdev.com>
 *   constructor.
 *   default.
 *   define special 'locked' and 'empty' key values in the ctor
 *   desired value.
 *   each allocation), and its allocate() method must take a raw number of
 *   EqualityComparable.  (Most of these are probably not something
 *   erased key will never be reused. If there's an associated value, we won't
 *   faster because of reduced data indirection.
 *   fitness for a particular purpose and noninfringement. In no event shall the
 *   fitness for a particular purpose and noninfringement. In no event shall the
 *   fitness for a particular purpose and noninfringement. In no event shall the
 *   frequently useful for this container (to avoid sprinkling
 *   give better memory utilization but probe lengths increase, reducing
 *   http://www.apache.org/licenses/LICENSE-2.0
 *   http://www.apache.org/licenses/LICENSE-2.0
 *   http://www.apache.org/licenses/LICENSE-2.0
 *   http://www.apache.org/licenses/LICENSE-2.0
 *   http://www.apache.org/licenses/LICENSE-2.0
 *   http://www.apache.org/licenses/LICENSE-2.0
 *   http://www.apache.org/licenses/LICENSE-2.0
 *   http://www.apache.org/licenses/LICENSE-2.0
 *   http://www.apache.org/licenses/LICENSE-2.0
 *   http://www.apache.org/licenses/LICENSE-2.0
 *   implemented.  It is a little too easy to misuse these functions
 *   implied, including but not limited to the warranties of merchantability,
 *   implied, including but not limited to the warranties of merchantability,
 *   implied, including but not limited to the warranties of merchantability,
 *   Insert returns false if there is a key collision and throws if the max size
 *   insertion happens for a new key, it will atomically have the
 *   is completely wait-free and doesn't require any non-relaxed atomic
 *   iterators, although this could change.
 *   Lefteris Karapetsas <lefteris@ethdev.com>
 *   liability, whether in an action of contract, tort or otherwise, arising from,
 *   liability, whether in an action of contract, tort or otherwise, arising from,
 *   liability, whether in an action of contract, tort or otherwise, arising from,
 *   make_pair everywhere), and providing both can lead to some gross
 *   Memory is not freed or reclaimed by erase, i.e. the cell containing the
 *   not be free or reclaimed.
 *   of key and returns true, or if key does not exist returns false and
 *   of the map is exceeded.
 *   one thread can be using the container to do that).
 *   operations.  AHA cannot grow beyond initialization capacity, but is
 *   out of or in connection with the Software or the use or other dealings in the
 *   out of or in connection with the Software or the use or other dealings in the
 *   out of or in connection with the Software or the use or other dealings in the
 *   performance.
 *   reserve(), or equal_range().  Also no constructors taking
 *   ret.index = capacity_.  Also sets ret.second to cell value, thus if insert
 *   ret.index is set to capacity_.
 *   returns 1 iff the key was located and marked as erased, and 0 otherwise.
 *   Returns false on failure due to key collision or full.
 *   See folly/tests/AtomicHashMapTest.cpp for more benchmarks.
 *   Sets ret.second to value found and ret.index to index
 *   Simple performance/memory tradeoff with maxLoadFactor.  Higher load factors
 *   Software.
 *   Software.
 *   Software.
 *   sub-maps are allocated on the fly and are processed in series, so the more
 *   successful this will be what we just inserted, if there is a key collision
 *   template error messages.
 *   there are (from growing past initial capacity), the worse the performance.
 *   This will attempt to erase the given key key_in if the key is found. It
 *   this will be the previously inserted value, and if the map is full it is
 *   touch it either.
 *   unique <int64, int64> entries on a 4-core, 2.5 GHz machine:
 *   wait-free for lookups.
 *   we do provide an insert(key, value).  The latter seems more
 *   with this container, where part of the point is that when an
 *   writing a cell, the key is locked while the rest of the record is
 *   written.  Once done, the cell is unlocked by setting the key.  find()
 *   you actually want to do with this anyway.)
 *  @author Jordan DeLong <delong.j@fb.com>
 *  @author Spencer Ahrens <sahrens@fb.com>
 *  AtomicHashArray is the building block for AtomicHashMap.  It provides the
 *  Check out AtomicHashMap.h for more thorough documentation on perf and
 *  constructor, for example).  If you're confident that you won't run out of
 *  core lock-free functionality, but is limited by the fact that it cannot
 *  feel free to use AHA directly.
 *  general pros and cons relative to other hash maps.
 *  grow past its initialization size and is a little more awkward (no public
 *  space, don't mind the awkardness, and really need bare-metal performance,
 * "number of iterations". Consider:
 * (iteration occurs outside the function).
 * - Efficiently thread safe for inserts (main point of this stuff),
 * - KeyT must be a 32 bit or 64 bit atomic integer type, and you must
 * - Several insertion functions, notably operator[], are not
 * - The above copyright notice and this permission notice shall be included in
 * - The above copyright notice and this permission notice shall be included in