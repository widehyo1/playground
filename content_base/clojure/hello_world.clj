playground/content_base/clojure on  main ❯ clj
Downloading: org/clojure/clojure/1.12.0/clojure-1.12.0.pom from central
Downloading: org/clojure/spec.alpha/0.5.238/spec.alpha-0.5.238.pom from central
Downloading: org/clojure/core.specs.alpha/0.4.74/core.specs.alpha-0.4.74.pom from central
Downloading: org/clojure/pom.contrib/1.2.0/pom.contrib-1.2.0.pom from central
Downloading: org/clojure/core.specs.alpha/0.4.74/core.specs.alpha-0.4.74.jar from central
Downloading: org/clojure/spec.alpha/0.5.238/spec.alpha-0.5.238.jar from central
Downloading: org/clojure/clojure/1.12.0/clojure-1.12.0.jar from central
Clojure 1.12.0
(+ 3 4)
7
(1 2 3)
Execution error (ClassCastException) at user/eval3 (REPL:1).
class java.lang.Long cannot be cast to class clojure.lang.IFn (java.lang.Long is in module java.base of loader 'bootstrap'; clojure.lang.IFn is in unnamed module of loader 'app')
'(1 2 3)
(1 2 3)
(+ 10 *1)
Execution error (ClassCastException) at user/eval7 (REPL:1).
class clojure.lang.PersistentList cannot be cast to class java.lang.Number (clojure.lang.PersistentList is in unnamed module of loader 'app'; java.lang.Number is in module java.base of loader 'bootstrap')
(+ 3 4)
7
(+ 10 *1)
17
(+ *1 *2)
24
(require '[clojure.repl :refer :all])
nil
(doc +)
-------------------------
clojure.core/+
([] [x] [x y] [x y & more])
  Returns the sum of nums. (+) returns 0. Does not auto-promote
  longs, will throw on overflow. See also: +'
nil
(doc doc)
-------------------------
clojure.repl/doc
([name])
Macro
  Prints documentation for a var or special form given its name,
   or for a spec if given a keyword
nil
(apropos "+")
(clojure.core/+ clojure.core/+' clojure.core/read+string clojure.spec.alpha/+ clojure.spec.alpha/rep+impl)
(find-doc "trim")
-------------------------
clojure.string/trim
([s])
  Removes whitespace from both ends of string.
-------------------------
clojure.string/trim-newline
([s])
  Removes all trailing newline \n or return \r characters from
  string.  Similar to Perl's chomp.
-------------------------
clojure.string/triml
([s])
  Removes whitespace from the left side of string.
-------------------------
clojure.string/trimr
([s])
  Removes whitespace from the right side of string.
-------------------------
clojure.pprint/ltrim
([s c])
  Trim all instances of c from the beginning of sequence s
-------------------------
clojure.pprint/rtrim
([s c])
  Trim all instances of c from the end of sequence s
-------------------------
clojure.core/read+string
([] [stream] [stream eof-error? eof-value] [stream eof-error? eof-value recursive?] [opts stream])
  Like read, and taking the same args. stream must be a LineNumberingPushbackReader.
  Returns a vector containing the object read and the (whitespace-trimmed) string read.
-------------------------
clojure.core/subvec
([v start] [v start end])
  Returns a persistent vector of the items in vector from
  start (inclusive) to end (exclusive).  If end is not supplied,
  defaults to (count vector). This operation is O(1) and very fast, as
  the resulting vector shares structure with the original and no
  trimming is done.
nil
(doc trim)
nil
(doc ltrim)
nil
(dir clojure.repl)
apropos
demunge
dir
dir-fn
doc
find-doc
pst
root-cause
set-break-handler!
source
source-fn
stack-element-str
thread-stopper
nil
(source dir)
(defmacro dir
  "Prints a sorted directory of public vars in a namespace"
  [nsname]
  `(doseq [v# (dir-fn '~nsname)]
     (println v#)))
nil
(def x 7)
#'user/x
(+ x x)
14
(println "what is this:" (+ 1 2))
what is this: 3
nil
(prn "one\n\ttwo")
"one\n\ttwo"
nil
(print "test\t\n")
test
nil
(print "test\t\ntest")
test
testnil
(println "test\t\ntest")
test
test
nil
(prn "test\t\ntest")
"test\t\ntest"
nil
(pr "test\t\ntest")
"test\t\ntest"nil
(+ 7654 1234)
8888
(/ (+ (+ 7 (* 3 4)) 5) 10)
12/5
(find-doc "rem")
-------------------------
clojure.java.javadoc/add-remote-javadoc
([package-prefix url])
  Adds to the list of remote Javadoc URLs.  package-prefix is the
  beginning of the package name that has docs at this URL.
-------------------------
clojure.java.javadoc/javadoc
([class-or-object])
  Opens a browser window displaying the javadoc for the argument.
  Tries *local-javadocs* first, then *remote-javadocs*.
-------------------------
clojure.java.javadoc/javadoc-url
([classname])
  Searches for a URL for the given class name.  Tries
  *local-javadocs* first, then *remote-javadocs*.  Returns a string.
-------------------------
clojure.java.process/start
([& opts+args])
  Start an external command, defined in args.
  The process environment vars are inherited from the parent by
  default (use :clear-env to clear them).

  If needed, provide options in map as first arg:
    :in - a ProcessBuilder.Redirect (default = :pipe) or :inherit
    :out - a ProcessBuilder.Redirect (default = :pipe) or :inherit :discard
    :err - a ProcessBuilder.Redirect (default = :pipe) or :inherit :discard :stdout
    :dir - current directory when the process runs (default=".")
    :clear-env - if true, remove all inherited parent env vars
    :env - {env-var value} of environment variables to set (all strings)

  Returns the java.lang.Process.
-------------------------
clojure.core.server/remote-prepl
([host port in-reader out-fn & {:keys [valf readf], :or {valf read-string, readf (fn* [p1__9119# p2__9120#] (read p1__9119# false p2__9120#))}}])
  Implements a prepl on in-reader and out-fn by forwarding to a
  remote [io-]prepl over a socket.  Messages will be read by readf, a
  fn of a LineNumberingPushbackReader and EOF value or a symbol naming
  same (default #(read %1 false %2)),
  :ret and :tap vals will be processed by valf, a fn of one argument
  or a symbol naming same (default read-string). If that function
  throws, :val will be unprocessed.

  Alpha, subject to change.
-------------------------
clojure.pprint/cl-format
([writer format-in & args])
  An implementation of a Common Lisp compatible format function. cl-format formats its
arguments to an output stream or string based on the format control string given. It
supports sophisticated formatting of structured data.

Writer is an instance of java.io.Writer, true to output to *out* or nil to output
to a string, format-in is the format control string and the remaining arguments
are the data to be formatted.

The format control string is a string to be output with embedded 'format directives'
describing how to format the various arguments passed in.

If writer is nil, cl-format returns the formatted result string. Otherwise, cl-format
returns nil.

For example:
 (let [results [46 38 22]]
        (cl-format true "There ~[are~;is~:;are~]~:* ~d result~:p: ~{~d~^, ~}~%"
                   (count results) results))

Prints to *out*:
 There are 3 results: 46, 38, 22

Detailed documentation on format control strings is available in the "Common Lisp the
Language, 2nd edition", Chapter 22 (available online at:
http://www.cs.cmu.edu/afs/cs.cmu.edu/project/ai-repository/ai/html/cltl/clm/node200.html#SECTION002633000000000000000)
and in the Common Lisp HyperSpec at
http://www.lispworks.com/documentation/HyperSpec/Body/22_c.htm

-------------------------
clojure.pprint/pprint-tab
([kind colnum colinc])
  Tab at this point in the pretty printing stream. kind specifies whether the tab
is :line, :section, :line-relative, or :section-relative.

Colnum and colinc specify the target column and the increment to move the target
forward if the output is already past the original target.

This function is intended for use when writing custom dispatch functions.

Output is sent to *out* which must be a pretty printing writer.

THIS FUNCTION IS NOT YET IMPLEMENTED.
-------------------------
clojure.pprint/remainders
([base val])
  Return the list of remainders (essentially the 'digits') of val in the given base
-------------------------
clojure.core/*clojure-version*
  The version info for Clojure core, as a map containing :major :minor
  :incremental and :qualifier keys. Feature releases may increment
  :minor and/or :major, bugfix releases will increment :incremental.
  Possible values of :qualifier include "GA", "SNAPSHOT", "RC-x" "BETA-x"
-------------------------
clojure.core/*print-length*
  *print-length* controls how many items of each collection the
  printer will print. If it is bound to logical false, there is no
  limit. Otherwise, it must be bound to an integer indicating the maximum
  number of items of each collection to print. If a collection contains
  more items, the printer will print items up to the limit followed by
  '...' to represent the remaining items. The root binding is nil
  indicating no limit.
-------------------------
clojure.core/add-tap
([f])
  adds f, a fn of one argument, to the tap set. This function will be called with anything sent via tap>.
  This function may (briefly) block (e.g. for streams), and will never impede calls to tap>,
  but blocking indefinitely may cause tap values to be dropped.
  Remember f in order to remove-tap
-------------------------
clojure.core/add-watch
([reference key fn])
  Adds a watch function to an agent/atom/var/ref reference. The watch
  fn must be a fn of 4 args: a key, the reference, its old-state, its
  new-state. Whenever the reference's state might have been changed,
  any registered watches will have their functions called. The watch fn
  will be called synchronously, on the agent's thread if an agent,
  before any pending sends if agent or ref. Note that an atom's or
  ref's state may have changed again prior to the fn call, so use
  old/new-state rather than derefing the reference. Note also that watch
  fns may be called from multiple threads simultaneously. Var watchers
  are triggered only by root binding changes, not thread-local
  set!s. Keys must be unique per reference, and can be used to remove
  the watch with remove-watch, but are otherwise considered opaque by
  the watch mechanism.
-------------------------
clojure.core/dedupe
([] [coll])
  Returns a lazy sequence removing consecutive duplicates in coll.
  Returns a transducer when no collection is provided.
-------------------------
clojure.core/deftype
([name [& fields] & opts+specs])
Macro
  (deftype name [fields*]  options* specs*)

  Options are expressed as sequential keywords and arguments (in any order).

  Supported options:
  :load-ns - if true, importing the type class will cause the
             namespace in which the type was defined to be loaded.
             Defaults to false.

  Each spec consists of a protocol or interface name followed by zero
  or more method bodies:

  protocol-or-interface-or-Object
  (methodName [args*] body)*

  Dynamically generates compiled bytecode for class with the given
  name, in a package with the same name as the current namespace, the
  given fields, and, optionally, methods for protocols and/or
  interfaces.

  The class will have the (by default, immutable) fields named by
  fields, which can have type hints. Protocols/interfaces and methods
  are optional. The only methods that can be supplied are those
  declared in the protocols/interfaces.  Note that method bodies are
  not closures, the local environment includes only the named fields,
  and those fields can be accessed directly. Fields can be qualified
  with the metadata :volatile-mutable true or :unsynchronized-mutable
  true, at which point (set! afield aval) will be supported in method
  bodies. Note well that mutable fields are extremely difficult to use
  correctly, and are present only to facilitate the building of higher
  level constructs, such as Clojure's reference types, in Clojure
  itself. They are for experts only - if the semantics and
  implications of :volatile-mutable or :unsynchronized-mutable are not
  immediately apparent to you, you should not be using them.

  Method definitions take the form:

  (methodname [args*] body)

  The argument and return types can be hinted on the arg and
  methodname symbols. If not supplied, they will be inferred, so type
  hints should be reserved for disambiguation.

  Methods should be supplied for all methods of the desired
  protocol(s) and interface(s). You can also define overrides for
  methods of Object. Note that a parameter must be supplied to
  correspond to the target object ('this' in Java parlance). Thus
  methods for interfaces will take one more argument than do the
  interface declarations. Note also that recur calls to the method
  head should *not* pass the target object, it will be supplied
  automatically and can not be substituted.

  In the method bodies, the (unqualified) name can be used to name the
  class (for calls to new, instance? etc).

  When AOT compiling, generates compiled bytecode for a class with the
  given name (a symbol), prepends the current ns as the package, and
  writes the .class file to the *compile-path* directory.

  One constructor will be defined, taking the designated fields.  Note
  that the field names __meta, __extmap, __hash and __hasheq are currently
  reserved and should not be used when defining your own types.

  Given (deftype TypeName ...), a factory function called ->TypeName
  will be defined, taking positional parameters for the fields
-------------------------
clojure.core/distinct
([] [coll])
  Returns a lazy sequence of the elements of coll with duplicates removed.
  Returns a stateful transducer when no collection is provided.
-------------------------
clojure.core/map
([f] [f coll] [f c1 c2] [f c1 c2 c3] [f c1 c2 c3 & colls])
  Returns a lazy sequence consisting of the result of applying f to
  the set of first items of each coll, followed by applying f to the
  set of second items in each coll, until any one of the colls is
  exhausted.  Any remaining items in other colls are ignored. Function
  f should accept number-of-colls arguments. Returns a transducer when
  no collection is provided.
-------------------------
clojure.core/mapv
([f coll] [f c1 c2] [f c1 c2 c3] [f c1 c2 c3 & colls])
  Returns a vector consisting of the result of applying f to the
  set of first items of each coll, followed by applying f to the set
  of second items in each coll, until any one of the colls is
  exhausted.  Any remaining items in other colls are ignored. Function
  f should accept number-of-colls arguments.
-------------------------
clojure.core/rem
([num div])
  remainder of dividing numerator by denominator.
-------------------------
clojure.core/remove
([pred] [pred coll])
  Returns a lazy sequence of the items in coll for which
  (pred item) returns logical false. pred must be free of side-effects.
  Returns a transducer when no collection is provided.
-------------------------
clojure.core/remove-all-methods
([multifn])
  Removes all of the methods of multimethod.
-------------------------
clojure.core/remove-method
([multifn dispatch-val])
  Removes the method of multimethod associated with dispatch-value.
-------------------------
clojure.core/remove-ns
([sym])
  Removes the namespace named by the symbol. Use with caution.
  Cannot be used to remove the clojure namespace.
-------------------------
clojure.core/remove-tap
([f])
  Remove f from the tap set.
-------------------------
clojure.core/remove-watch
([reference key])
  Removes a watch (set by add-watch) from a reference
-------------------------
clojure.core/require
([& args])
  Loads libs, skipping any that are already loaded. Each argument is
  either a libspec that identifies a lib, a prefix list that identifies
  multiple libs whose names share a common prefix, or a flag that modifies
  how all the identified libs are loaded. Use :require in the ns macro
  in preference to calling this directly.

  Libs

  A 'lib' is a named set of resources in classpath whose contents define a
  library of Clojure code. Lib names are symbols and each lib is associated
  with a Clojure namespace and a Java package that share its name. A lib's
  name also locates its root directory within classpath using Java's
  package name to classpath-relative path mapping. All resources in a lib
  should be contained in the directory structure under its root directory.
  All definitions a lib makes should be in its associated namespace.

  'require loads a lib by loading its root resource. The root resource path
  is derived from the lib name in the following manner:
  Consider a lib named by the symbol 'x.y.z; it has the root directory
  <classpath>/x/y/, and its root resource is <classpath>/x/y/z.clj, or
  <classpath>/x/y/z.cljc if <classpath>/x/y/z.clj does not exist. The
  root resource should contain code to create the lib's
  namespace (usually by using the ns macro) and load any additional
  lib resources.

  Libspecs

  A libspec is a lib name or a vector containing a lib name followed by
  options expressed as sequential keywords and arguments.

  Recognized options:
  :as takes a symbol as its argument and makes that symbol an alias to the
    lib's namespace in the current namespace.
  :as-alias takes a symbol as its argument and aliases like :as, however
    the lib will not be loaded. If the lib has not been loaded, a new
    empty namespace will be created (as with create-ns).
  :refer takes a list of symbols to refer from the namespace or the :all
    keyword to bring in all public vars.

  Prefix Lists

  It's common for Clojure code to depend on several libs whose names have
  the same prefix. When specifying libs, prefix lists can be used to reduce
  repetition. A prefix list contains the shared prefix followed by libspecs
  with the shared prefix removed from the lib names. After removing the
  prefix, the names that remain must not contain any periods.

  Flags

  A flag is a keyword.
  Recognized flags: :reload, :reload-all, :verbose
  :reload forces loading of all the identified libs even if they are
    already loaded (has no effect on libspecs using :as-alias)
  :reload-all implies :reload and also forces loading of all libs that the
    identified libs directly or indirectly load via require or use
    (has no effect on libspecs using :as-alias)
  :verbose triggers printing information about each load, alias, and refer

  Example:

  The following would load the libraries clojure.zip and clojure.set
  abbreviated as 's'.

  (require '(clojure zip [set :as s]))
-------------------------
clojure.core/restart-agent
([a new-state & options])
  When an agent is failed, changes the agent state to new-state and
  then un-fails the agent so that sends are allowed again.  If
  a :clear-actions true option is given, any actions queued on the
  agent that were being held while it was failed will be discarded,
  otherwise those held actions will proceed.  The new-state must pass
  the validator if any, or restart will throw an exception and the
  agent will remain failed with its old state and error.  Watchers, if
  any, will NOT be notified of the new state.  Throws an exception if
  the agent is not failed.
-------------------------
clojure.core/sequence
([coll] [xform coll] [xform coll & colls])
  Coerces coll to a (possibly empty) sequence, if it is not already
  one. Will not force a lazy seq. (sequence nil) yields (), When a
  transducer is supplied, returns a lazy sequence of applications of
  the transform to the items in coll(s), i.e. to the set of first
  items of each coll, followed by the set of second
  items in each coll, until any one of the colls is exhausted.  Any
  remaining items in other colls are ignored. The transform should accept
  number-of-colls arguments
-------------------------
clojure.core/unchecked-remainder-int
([x y])
  Returns the remainder of division of x by y, both int.
  Note - uses a primitive operator subject to truncation.
-------------------------
clojure.spec.alpha/def
([k spec-form])
Macro
  Given a namespace-qualified keyword or resolvable symbol k, and a
  spec, spec-name, predicate or regex-op makes an entry in the
  registry mapping k to the spec. Use nil to remove an entry in
  the registry for k.
nil
(find-doc "mod")
-------------------------
clojure.java.basis/current-basis
([])
  Return the current basis, which may have been modified since runtime launch.
-------------------------
clojure.java.io/IOFactory
  Factory functions that create ready-to-use, buffered versions of
   the various Java I/O stream types, on top of anything that can
   be unequivocally converted to the requested kind of stream.

   Common options include

     :append    true to open stream in append mode
     :encoding  string name of encoding to use, e.g. "UTF-8".

   Callers should generally prefer the higher level API provided by
   reader, writer, input-stream, and output-stream.
-------------------------
clojure.pprint/*print-pprint-dispatch*
  The pretty print dispatch function. Use with-pprint-dispatch or set-pprint-dispatch
to modify.
-------------------------
clojure.pprint/write
([object & kw-args])
  Write an object subject to the current bindings of the printer control variables.
Use the kw-args argument to override individual variables for this call (and any
recursive calls). Returns the string result if :stream is nil or nil otherwise.

The following keyword arguments can be passed with values:
  Keyword              Meaning                              Default value
  :stream              Writer for output or nil             true (indicates *out*)
  :base                Base to use for writing rationals    Current value of *print-base*
  :circle*             If true, mark circular structures    Current value of *print-circle*
  :length              Maximum elements to show in sublists Current value of *print-length*
  :level               Maximum depth                        Current value of *print-level*
  :lines*              Maximum lines of output              Current value of *print-lines*
  :miser-width         Width to enter miser mode            Current value of *print-miser-width*
  :dispatch            The pretty print dispatch function   Current value of *print-pprint-dispatch*
  :pretty              If true, do pretty printing          Current value of *print-pretty*
  :radix               If true, prepend a radix specifier   Current value of *print-radix*
  :readably*           If true, print readably              Current value of *print-readably*
  :right-margin        The column for the right margin      Current value of *print-right-margin*
  :suppress-namespaces If true, no namespaces in symbols    Current value of *print-suppress-namespaces*

  * = not yet supported

-------------------------
clojure.core/agent
([state & options])
  Creates and returns an agent with an initial value of state and
  zero or more options (in any order):

  :meta metadata-map

  :validator validate-fn

  :error-handler handler-fn

  :error-mode mode-keyword

  If metadata-map is supplied, it will become the metadata on the
  agent. validate-fn must be nil or a side-effect-free fn of one
  argument, which will be passed the intended new state on any state
  change. If the new state is unacceptable, the validate-fn should
  return false or throw an exception.  handler-fn is called if an
  action throws an exception or if validate-fn rejects a new state --
  see set-error-handler! for details.  The mode-keyword may be either
  :continue (the default if an error-handler is given) or :fail (the
  default if no error-handler is given) -- see set-error-mode! for
  details.
-------------------------
clojure.core/derive
([tag parent] [h tag parent])
  Establishes a parent/child relationship between parent and
  tag. Parent must be a namespace-qualified symbol or keyword and
  child can be either a namespace-qualified symbol or keyword or a
  class. h must be a hierarchy obtained from make-hierarchy, if not
  supplied defaults to, and modifies, the global hierarchy.
-------------------------
clojure.core/ensure
([ref])
  Must be called in a transaction. Protects the ref from modification
  by other transactions.  Returns the in-transaction-value of
  ref. Allows for more concurrency than (ref-set ref @ref)
-------------------------
clojure.core/error-mode
([a])
  Returns the error-mode of agent a.  See set-error-mode!
-------------------------
clojure.core/for
([seq-exprs body-expr])
Macro
  List comprehension. Takes a vector of one or more
   binding-form/collection-expr pairs, each followed by zero or more
   modifiers, and yields a lazy sequence of evaluations of expr.
   Collections are iterated in a nested fashion, rightmost fastest,
   and nested coll-exprs can refer to bindings created in prior
   binding-forms.  Supported modifiers are: :let [binding-form expr ...],
   :while test, :when test.

  (take 100 (for [x (range 100000000) y (range 1000000) :while (< y x)] [x y]))
-------------------------
clojure.core/mod
([num div])
  Modulus of num and div. Truncates toward negative infinity.
-------------------------
clojure.core/require
([& args])
  Loads libs, skipping any that are already loaded. Each argument is
  either a libspec that identifies a lib, a prefix list that identifies
  multiple libs whose names share a common prefix, or a flag that modifies
  how all the identified libs are loaded. Use :require in the ns macro
  in preference to calling this directly.

  Libs

  A 'lib' is a named set of resources in classpath whose contents define a
  library of Clojure code. Lib names are symbols and each lib is associated
  with a Clojure namespace and a Java package that share its name. A lib's
  name also locates its root directory within classpath using Java's
  package name to classpath-relative path mapping. All resources in a lib
  should be contained in the directory structure under its root directory.
  All definitions a lib makes should be in its associated namespace.

  'require loads a lib by loading its root resource. The root resource path
  is derived from the lib name in the following manner:
  Consider a lib named by the symbol 'x.y.z; it has the root directory
  <classpath>/x/y/, and its root resource is <classpath>/x/y/z.clj, or
  <classpath>/x/y/z.cljc if <classpath>/x/y/z.clj does not exist. The
  root resource should contain code to create the lib's
  namespace (usually by using the ns macro) and load any additional
  lib resources.

  Libspecs

  A libspec is a lib name or a vector containing a lib name followed by
  options expressed as sequential keywords and arguments.

  Recognized options:
  :as takes a symbol as its argument and makes that symbol an alias to the
    lib's namespace in the current namespace.
  :as-alias takes a symbol as its argument and aliases like :as, however
    the lib will not be loaded. If the lib has not been loaded, a new
    empty namespace will be created (as with create-ns).
  :refer takes a list of symbols to refer from the namespace or the :all
    keyword to bring in all public vars.

  Prefix Lists

  It's common for Clojure code to depend on several libs whose names have
  the same prefix. When specifying libs, prefix lists can be used to reduce
  repetition. A prefix list contains the shared prefix followed by libspecs
  with the shared prefix removed from the lib names. After removing the
  prefix, the names that remain must not contain any periods.

  Flags

  A flag is a keyword.
  Recognized flags: :reload, :reload-all, :verbose
  :reload forces loading of all the identified libs even if they are
    already loaded (has no effect on libspecs using :as-alias)
  :reload-all implies :reload and also forces loading of all libs that the
    identified libs directly or indirectly load via require or use
    (has no effect on libspecs using :as-alias)
  :verbose triggers printing information about each load, alias, and refer

  Example:

  The following would load the libraries clojure.zip and clojure.set
  abbreviated as 's'.

  (require '(clojure zip [set :as s]))
-------------------------
clojure.core/set-error-mode!
([a mode-keyword])
  Sets the error-mode of agent a to mode-keyword, which must be
  either :fail or :continue.  If an action being run by the agent
  throws an exception or doesn't pass the validator fn, an
  error-handler may be called (see set-error-handler!), after which,
  if the mode is :continue, the agent will continue as if neither the
  action that caused the error nor the error itself ever happened.

  If the mode is :fail, the agent will become failed and will stop
  accepting new 'send' and 'send-off' actions, and any previously
  queued actions will be held until a 'restart-agent'.  Deref will
  still work, returning the state of the agent before the error.
-------------------------
clojure.core/sort
([coll] [comp coll])
  Returns a sorted sequence of the items in coll. If no comparator is
  supplied, uses compare.  comparator must implement
  java.util.Comparator.  Guaranteed to be stable: equal elements will
  not be reordered.  If coll is a Java array, it will be modified.  To
  avoid this, sort a copy of the array.
-------------------------
clojure.core/sort-by
([keyfn coll] [keyfn comp coll])
  Returns a sorted sequence of the items in coll, where the sort
  order is determined by comparing (keyfn item).  If no comparator is
  supplied, uses compare.  comparator must implement
  java.util.Comparator.  Guaranteed to be stable: equal elements will
  not be reordered.  If coll is a Java array, it will be modified.  To
  avoid this, sort a copy of the array.
-------------------------
clojure.core/underive
([tag parent] [h tag parent])
  Removes a parent/child relationship between parent and
  tag. h must be a hierarchy obtained from make-hierarchy, if not
  supplied defaults to, and modifies, the global hierarchy.
-------------------------
clojure.core/vec
([coll])
  Creates a new vector containing the contents of coll. Java arrays
  will be aliased and should not be modified.
-------------------------
clojure.core/with-precision
([precision & exprs])
Macro
  Sets the precision and rounding mode to be used for BigDecimal operations.

  Usage: (with-precision 10 (/ 1M 3))
  or:    (with-precision 10 :rounding HALF_DOWN (/ 1M 3))

  The rounding mode is one of CEILING, FLOOR, HALF_UP, HALF_DOWN,
  HALF_EVEN, UP, DOWN and UNNECESSARY; it defaults to HALF_UP.
-------------------------
clojure.java.basis
  The lib basis includes which libraries and versions were loaded both
  for direct dependencies and transitive dependencies, as well as the
  classpath and possibly other information from the resolution process.
  This basis will be known if the runtime was started by the Clojure CLI.

  The Clojure CLI or tools.deps merge a set of deps maps (often from
  deps.edn files). Additional runtime modifications are supplied via argmap
  keys, provided via alias maps in the merged deps. Deps maps typically have
  :paths, :deps, and :aliases keys.

  The basis is a superset of merged deps.edn files with the following
  additional keys:
    :basis-config - params used to configure basis deps sources, can be
                    string path, deps map, nil, or :default
      :root - default = loaded as a resource from tools.deps)
      :user - default = ~/.clojure/deps.edn)
      :project - default = ./deps.edn)
      :extra - default = nil
      :aliases - coll of keyword aliases to include during dep calculation
    :argmap - effective argmap (after resolving and merging argmaps from aliases)
    :libs - map of lib to coord for all included libraries
    :classpath - classpath map, keys are paths (to directory or .jar), values
                 are maps with source identifier (either :lib-name or :path-key)
    :classpath-roots - vector of paths in classpath order (keys of :classpath)
-------------------------
clojure.pprint
  A Pretty Printer for Clojure

clojure.pprint implements a flexible system for printing structured data
in a pleasing, easy-to-understand format. Basic use of the pretty printer is
simple, just call pprint instead of println. More advanced users can use
the building blocks provided to create custom output formats.

Out of the box, pprint supports a simple structured format for basic data
and a specialized format for Clojure source code. More advanced formats,
including formats that don't look like Clojure data at all like XML and
JSON, can be rendered by creating custom dispatch functions.

In addition to the pprint function, this module contains cl-format, a text
formatting function which is fully compatible with the format function in
Common Lisp. Because pretty printing directives are directly integrated with
cl-format, it supports very concise custom dispatch. It also provides
a more powerful alternative to Clojure's standard format function.

See documentation for pprint and cl-format for more information or
complete documentation on the Clojure web site on GitHub.
-------------------------
clojure.repl.deps
  clojure.repl.deps provides facilities for dynamically modifying the available
  libraries in the runtime when running at the REPL, without restarting
nil
(doc rem)
-------------------------
clojure.core/rem
([num div])
  remainder of dividing numerator by denominator.
nil
(doc mod)
-------------------------
clojure.core/mod
([num div])
  Modulus of num and div. Truncates toward negative infinity.
nil
(find-doc "stack")
-------------------------
clojure.main/demunge
([fn-name])
  Given a string representation of a fn class,
  as in a stack trace element, returns a readable version.
-------------------------
clojure.main/stack-element-str
([el])
  Returns a (possibly unmunged) string representation of a StackTraceElement
-------------------------
clojure.repl/demunge
([fn-name])
  Given a string representation of a fn class,
  as in a stack trace element, returns a readable version.
-------------------------
clojure.repl/pst
([] [e-or-depth] [e depth])
  Prints a stack trace of the exception, to the depth requested. If none supplied, uses the root cause of the
  most recent repl exception (*e), and a depth of 12.
-------------------------
clojure.repl/stack-element-str
([el])
  Returns a (possibly unmunged) string representation of a StackTraceElement
-------------------------
clojure.core/*pending-paths*
  A stack of paths currently being loaded by this thread
-------------------------
clojure.core/Throwable->map
([o])
  Constructs a data representation for a Throwable with keys:
    :cause - root cause message
    :phase - error phase
    :via - cause chain, with cause keys:
             :type - exception class symbol
             :message - exception message
             :data - ex-data
             :at - top stack element
    :trace - root cause stack elements
-------------------------
clojure.core/trampoline
([f] [f & args])
  trampoline can be used to convert algorithms requiring mutual
  recursion without stack consumption. Calls f with supplied args, if
  any. If f returns a fn, calls that fn with no arguments, and
  continues to repeat, until the return value is not a fn, then
  returns that non-fn value. Note that if you want to return a fn as a
  final value, you must wrap it in some data structure and unpack it
  after trampoline returns.
nil
exit
Syntax error compiling at (REPL:0:0).
Unable to resolve symbol: exit in this context
user=>
playground/content_base/clojure on  main took 2m39s ❯ clj
Clojure 1.12.0
(defn greet [name] (str "Hello, " name))
#'user/greet
(greet "students")
"Hello, students"
(defn messenger
([] (messenger "Hello world!"))
([msg] (println msg))
)
#'user/messenger
(messenger)
Hello world!
nil
(messenger "Hello class!")
Hello class!
nil
(defn hello [greeting & who]
  (println greeting who))
#'user/hello
(hello "Hello" "world" "class")
Hello (world class)
nil
(fn [message] (println message))
#object[user$eval145$fn__146 0x63e5e5b4 "user$eval145$fn__146@63e5e5b4"]
( (fn [message] (println message)) "Hello world!")
Hello world!
nil
#(+ 6 %)
#object[user$eval155$fn__156 0x7068f7ca "user$eval155$fn__156@7068f7ca"]
#(+ %1 %2)
#object[user$eval163$fn__164 0x6fca2a8f "user$eval163$fn__164@6fca2a8f"]
#(println %1 %2 %&)
#object[user$eval173$fn__174 0x41f35f7c "user$eval173$fn__174@41f35f7c"]
#(vector %)
#object[user$eval179$fn__180 0x7a639ec5 "user$eval179$fn__180@7a639ec5"]
(apply f '(1 2 3 4))
Syntax error compiling at (REPL:1:1).
Unable to resolve symbol: f in this context
(defn plot [shape coords]
(plotxy shape (first coords) (second coords)))
Syntax error compiling at (REPL:2:1).
Unable to resolve symbol: plotxy in this context
(defn plot [shape coords]
(apply plotxy shape coords))
Syntax error compiling at (REPL:2:1).
Unable to resolve symbol: plotxy in this context
(let [name value] (code that uses name))
Syntax error compiling at (REPL:1:1).
Unable to resolve symbol: value in this context
(let [x 1
y 2]
(+ x y))
3
(defn messenger [msg]
(let [a 7
b 5
c (clojure.string/capitalize msg)]
(println a b c)))
#'user/messenger
(messenger "test")
7 5 Test
nil
(defn messenger-builder [greeting]
(fn [who] (println greeting who)))
#'user/messenger-builder
(def hello-er (messenger-builder "Hello))


playground/content_base/clojure on  main took 14m21s ❯ cl
Command 'cl' not found, but can be installed with:
sudo apt install cl-launch

playground/content_base/clojure on  main ❯ clj
Clojure 1.12.0
(defn messenger-builder [greeting]
(fn [who] (println greeting who)))
#'user/messenger-builder
(def hello-er (messenger-builder "Hello"))
#'user/hello-er
(hello-er "world!")
Hello world!
nil
(defn greet [] (println "Hello"))
#'user/greet
(greet)
Hello
nil
(def greet (fn [] (println "Hello")))
#'user/greet
(greet)
Hello
nil
(def greet #(println "Hello"))
#'user/greet
(greet)
Hello
nil
(doc str)
-------------------------
clojure.core/str
([] [x] [x & ys])
  With no args, returns the empty string. With one arg x, returns
  x.toString().  (str nil) returns the empty string. With more than
  one arg, returns the concatenation of the str values of the args.
nil
(defn greeting
[] (str "Hello, World!")
[x] (str "Hello, " x)
[x y] (str x y)
)
Syntax error compiling at (REPL:1:1).
Unable to resolve symbol: x in this context
(defn greeting
([] (str "Hello, World!"))
([x] (str "Hello, " x))
([x y] (str x y)))
#'user/greeting
(assert (= "Hello, World!" (greeting)))
nil
(assert (= "Hello, Clojure!" (greeting "Clojure")))
Execution error (AssertionError) at user/eval153 (REPL:1).
Assert failed: (= "Hello, Clojure!" (greeting "Clojure"))
(assert (= "Good morning, Clojure!" (greeting "Good morning" "Clojure")))
Execution error (AssertionError) at user/eval155 (REPL:1).
Assert failed: (= "Good morning, Clojure!" (greeting "Good morning" "Clojure"))
(greeting "Good morning" "Clojure")
"Good morningClojure"
(greeting "Clojure")
"Hello, Clojure"
(defn greeting
([] (str "Hello, World!"))
([x] (str "Hello, " x "!"))
([x y] (str x ", " y "!")))
#'user/greeting
(assert (= "Good morning, Clojure!" (greeting "Good morning" "Clojure")))
nil
(assert (= "Hello, Clojure!" (greeting "Clojure")))
nil
(defn do-nothing [x] x)
#'user/do-nothing
(do-nothing 123)
123
(defn always-thing [x] 100)
#'user/always-thing
(always-thing 123)
100
(always-thing 1251)
100
(defn make-thingy [x]
(fn [y] x))
#'user/make-thingy
(let [n (rand-int Integer/MAX_VALUE)
      f (make-thingy n)]
(assert (= n (f)))
(assert (= n (f 123)))
(assert (= n (apply f 123 (range)))))
Execution error (ArityException) at user/eval177 (REPL:3).
Wrong number of args (0) passed to: user/make-thingy/fn--174
(defn triplicate [f] (apply '(f f f)))
#'user/triplicate
((triplicate str) "asdf")
Execution error (ArityException) at user/triplicate (REPL:1).
Wrong number of args (1) passed to: clojure.core/apply
user=>
