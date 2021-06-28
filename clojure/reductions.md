# Reductions and Reduce

Reduction is better know to C++ and Rust devs as `scan` algorithm. In python its known as accumulate(itertools).

Reductions take a collection(`C`) and a function(`F`). `F` is applied to every element in the `C`.
`C` takes two values I name them `a and e` (short for accumulator and element). It is awfully similar to reduce. 
The main difference is reduce returns a scalar and reduction returns a vector(collection).

consider the following codes




```clojure
(reductions + [1 1 1 1])
;(1 2 3 4)
(reductions + [1 2 3])
;(1 3 6)
(reduce + [1 2 3])
;6
(= (last (reduction func collection)) (reduce func collection)
; a difference between the above functions is that
; reduce doesnt store the accumulator value(itermediate value) in any manner
; wherease reduction pushes this itermediate value to a list and which is the final output
```


[Lets solve a euler problem using reduction](https://projecteuler.net/problem=5)

```clojure
(defn gcd [a b]
  "um yeah; good ol fashioned euclidean gcd calculation"
  (if (zero? b)
    a
    (gcd b (mod a b))
  )
)

(defn lcm [a b]
  (/ (* a b) (gcd a b))
)

(defn solve []
  ;hell yeah
  (println (last (reductions lcm (range 1 11))))
)
; drop reduction in favor of reduce
```
