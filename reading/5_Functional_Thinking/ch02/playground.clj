(ns trans.core
  (:require [clojure.string :as s]))

(defn process [list-of-emps]
  (reduce str (interpose ","
    (map s/capitalize (filter #(> (count %) 1) list-of-emps)))))

(defn process2 [list-of-emps]
  (->> list-of-emps
       (filter #(> (count %) 1))
       (map s/capitalize)
       (interpose ",")
       (reduce str)))

(comment
  (defn classify-value [x]
    (cond
      (= x 1) "one"
      (= x 2) "two"
      (even? x) "even"
      (odd? x) "odd"
      :else "unknown"))
)

(defn getFactors [number]
  (filter #(= (mod number %) 0) (range 1 number)))

(defn classifyNumber [number]
  (cond
    (= number (reduce + (getFactors number))) "perfect"
    (> number (reduce + (getFactors number))) "deficient"
    (< number (reduce + (getFactors number))) "abundant"
  )
)

(comment chatgpt
  (defn classifyNumber [number]
    (let [sum-of-factors (reduce + (getFactors number))]
      (cond
        (= number sum-of-factors) "perfect"
        (> number sum-of-factors) "deficient"
        (< number sum-of-factors) "abundant")))
)

(comment from book)

(defn classify [num]
  (let [factors (->> (range 1 (inc num))
                     (filter #(zero? (rem num %))))
        sum (reduce + factors)
        aliquot-sum (- sum num)]
  (cond
      (= aliquot-sum num) :perfect
      (> aliquot-sum num) :abundant
      (< aliquot-sum num) :deficient
  )))

(defn subtract-from-hundred (partial -100))

(subtract-from-hundred 10)
(subtract-from-hundred 10 20)
