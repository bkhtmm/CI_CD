from src.second_venv.primes_sum import is_prime, primes, checksum, pipeline


def test_primes():
    assert is_prime(7)
    assert not is_prime(10)


def test_length():
    assert len(primes(1000)) == 1000


def test_control_sum():
    assert checksum([1, 2, 6, 24]) == 6012369


def test_pipeline():
    assert type(pipeline()) is int


test_primes()
test_length()
test_control_sum()
test_pipeline()
