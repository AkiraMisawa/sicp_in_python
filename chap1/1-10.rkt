#lang racket
(define (A x y)
  (cond ((= y 0) 0)
        ((= x 0) (* 2 y))
        ((= y 1) 2)
        (else (A (- x 1) (A x (- y 1))))))

(= 1024 (A 1 10))
(= 65536 (A 2 4))
(= 65536 (A 3 3))

;; x is bounded to 0
;; (f n) : 2 * n
(define (f n) (A 0 n))
(= 2 (f 1))
(= 4 (f 2))
(= -6 (f -3))
(= 10 (f 5))

;; x is bounded to 1
;; (g n) : 2^n
(define (g n) (A 1 n))
(= 2 (g 1))
(= 4 (g 2))
(= 256 (g 8))
(= 1024 (g 10))

;; x is bounded to 2
;; (h n) : 2^(2^(2^(...)))
(define (h n) (A 2 n))
(= 2 (h 1))
(= 4 (h 2))
(= 16 (h 3))
(= 65536 (h 4))

;; (k n) : 5 * n^2
(define (k n) (* 5 n n))
(= 5 (k 1))
(= 5 (k -1))
(= 20 (k 2))
(= 125 (k 5))
