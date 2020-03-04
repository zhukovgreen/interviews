"""Solve the game "Guess a number".

find a secret integer between 1 and 1 000 000 in less than 50 guesses.
Write a function that solves the game without user input and returns the
solution by using the function verify() which is defined with the following
specification:
function verify(guess: integer) -> integer
Argument:
     guess (integer) the number to verify
Returns:
     0 if the guess is the solution, your program won
     -1 if the solution is smaller than the guess parameter
     1  if the solution is bigger than the guess parameter

Warning: You are not allowed to call verify() more that 50 times
or you loose."""


import logging
import sys

import pytest

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def state_repr(
    low_b: int, high_b: int, num_of_guesses: int, candidate: int
) -> str:
    return (
        f"|LB={low_b}|---------|{candidate}|----------|HB={high_b}|"
        f"\n num_of_guesses is {num_of_guesses}\n"
    )


SECRET_NUM = 5

LOW_BOUNARY = 1
MAX_BOUNDARY = 1_000_000
MAX_NUM_GUESSES = 50


def set_secret_to(val: int):
    global SECRET_NUM
    SECRET_NUM = val
    logger.debug(f"Secret changed to {val}")


def verify(guess: int) -> int:
    if guess == SECRET_NUM:
        return 0
    if guess > SECRET_NUM:
        return -1
    if guess < SECRET_NUM:
        return 1


def guesser(interactive=False) -> int:
    if interactive:
        new_secret = input("Enter a secret value: ")
        set_secret_to(int(new_secret))
    num_of_guesses = 0
    low_b = LOW_BOUNARY
    high_b = MAX_BOUNDARY
    while num_of_guesses <= MAX_NUM_GUESSES:
        num_of_guesses += 1
        candidate = (low_b + high_b) // 2
        logger.debug(
            f"Current state is "
            f"{state_repr(low_b, high_b, num_of_guesses, candidate)}"
        )
        if verify(candidate) == 0:
            logger.info("Guessed! Returning the value....\n")
            return candidate
        elif verify(candidate) == 1:
            low_b = candidate
        elif verify(candidate) == -1:
            high_b = candidate
    logger.info(
        f"Unable to fit in 50 guesses. Current state is: "
        f"{state_repr(low_b, high_b, num_of_guesses, candidate)}"
    )


@pytest.mark.parametrize(
    "secret, exp", [(1, 1), (100000, 100000), (50, 50), (0.6, None)]
)
def test_solution(secret, exp):
    set_secret_to(secret)
    assert guesser() == exp
