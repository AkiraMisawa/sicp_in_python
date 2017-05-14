#lang racket
(define (square x) (* x x))

(define (divides? a b) (= (remainder b a) 0))

(define (find-divisor n test-divisor)
  (cond ((> (square test-divisor) n) n)
        ((divides? test-divisor n) test-divisor)
        (else (find-divisor n (+ test-divisor 1)))))

(define (smallest-divisor n) (find-divisor n 2))

(define (prime? n)
  (= n (smallest-divisor n)))
;; runtime: システムが動いた時間を整数で返す(e.g. マイクロ秒で計測したもの)
;; racketにはないので定義する
(define (runtime) (current-milliseconds))

(define (timed-prime-test n)
  (newline)
  (display n)
  (start-prime-test n (runtime)))

(define (start-prime-test n start-time)
  (if (prime? n)
      (report-prime (- (runtime) start-time))
      (display "nya")))

(define (report-prime elapsed-time)
  (display " *** ")
  (display elapsed-time))

(define (search-for-primes n)
  (define (search-for-primes-iter i k)
    (cond ((=  k 3))
          ((prime? i) (display i) (newline) (search-for-primes-iter (+ i 2) (+ k 1)))
          (else (search-for-primes-iter (+ i 2) k))))
  (search-for-primes-iter n 0))

(search-for-primes 1001)
(search-for-primes 10001)
(search-for-primes 100001)

(timed-prime-test 1009)
(timed-prime-test 1013)
(timed-prime-test 1019)

(timed-prime-test 10007)
(timed-prime-test 10009)
(timed-prime-test 10037)

(timed-prime-test 100003)
(timed-prime-test 100019)
(timed-prime-test 100043)
