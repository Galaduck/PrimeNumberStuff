# Count the primes ≤ 1e10 using all CPU cores
primesieve 1e10

# Print the primes ≤ 1000000
primesieve 1000000 --print

# Store the primes ≤ 1000000 in a text file
primesieve 1000000 --print > primes.txt

# Print the twin primes ≤ 1000000
primesieve 1000000 --print=2

# Count the prime triplets inside [1e10, 1e10+2^32]
primesieve 1e10 --dist=2^32 --count=3

Usage: primesieve [START] STOP [OPTION]...
Generate the primes and/or prime k-tuplets inside [START, STOP]
(< 2^64) using the segmented sieve of Eratosthenes.

Options:
  -c, --count[=NUM+]         Count primes and/or prime k-tuplets, NUM <= 6.
                             Count primes: -c or --count (default option),
                             count twin primes: -c2 or --count=2,
                             count prime triplets: -c3 or --count=3, ...
      --cpu-info             Print CPU information (cache sizes).
  -d, --dist=DIST            Sieve the interval [START, START + DIST].
  -n, --nth-prime            Find the nth prime.
                             primesieve 100 -n: finds the 100th prime,
                             primesieve 2 100 -n: finds the 2nd prime > 100.
  -p, --print[=NUM]          Print primes or prime k-tuplets, NUM <= 6.
                             Print primes: -p or --print,
                             print twin primes: -p2 or --print=2,
                             print prime triplets: -p3 or --print=3, ...
  -q, --quiet                Quiet mode, prints less output.
  -s, --size=SIZE            Set the sieve size in KiB, SIZE <= 8192.
                             By default primesieve uses a sieve size that
                             matches your CPU's L1 cache size (per core) or is
                             slightly smaller than your CPU's L2 cache size.
  -S, --stress-test[=MODE]   Run a stress test. The MODE can be either
                             CPU (default) or RAM. The default timeout is 24h.
      --test                 Run various correctness tests (< 1 minute).
  -t, --threads=NUM          Set the number of threads, NUM <= CPU cores.
                             Default setting: use all available CPU cores.
      --time                 Print the time elapsed in seconds.
      --timeout=SEC          Set the stress test timeout in seconds. Supported
                             units of time suffixes: s, m, h, d or y.
                             30 minutes timeout: --timeout 30m