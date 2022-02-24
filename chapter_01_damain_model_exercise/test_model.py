'''
Date: 2021-12-08 21:08:08
Author: ChenRun
Description: 
'''
from datetime import date, timedelta

import pytest

from chapter_01_damain_model_exercise.model import Batch, Money, OrderLine, Name

tody = date.today()
tomorrow = tody + timedelta(days=1)
later = tomorrow + timedelta(days=10)


def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch("batch-001", sku, batch_qty, eta=date.today()),
        OrderLine("order-123", sku, line_qty)
    )


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    line = OrderLine("order-ref", "SMALL-TABLE", 2)

    batch.allocate(line)

    assert batch.available_quantity == 18


def test_can_anllocate_if_available_greater_than_required():
    large_batch, small_line = make_batch_and_line("ELEGANT-LAMP", 20, 2)
    assert large_batch.can_allocate(small_line)


def test_cannot_allocate_if_available_smaller_than_required():
    small_batch, large_line = make_batch_and_line("ELEGANT-LAMP", 2, 20)
    assert small_batch.can_allocate(large_line) is False


def test_can_allocate_if_available_equal_to_required():
    batch, line = make_batch_and_line("ELEGANT-LAMP", 2, 2)
    assert batch.can_allocate(line)


def test_prefers_warehouse_batches_to_shipmetns():
    batch = Batch("batch-001", "UNCOMFORTALE-CHAIR", 100, eta=None)
    different_sku_line = OrderLine("order-123", "EXPENSIVE-TOASTER", 10)
    assert batch.can_allocate(different_sku_line) is False


def test_can_only_deallocate_allocated_lines():
    batch, unallocated_line = make_batch_and_line("DECORATIVE-TRINKET", 20, 2)
    batch.deallocate(unallocated_line)
    assert batch.available_quantity == 20


fiver = Money("gbp", 5)
tenner = Money("gbp", 10)


def test_equality():
    assert Money("gbp", 10) == Money("gbp", 10)
    assert Name("Chen", "Run") != Name("Peng", "HuiXian")


def test_can_add_money_values_for_the_same_currency():
    assert fiver + fiver == tenner


def test_can_subtract_money_values():
    assert tenner - fiver == fiver


def test_adding_different_currencies_fails():
    with pytest.raises(ValueError):
        Money("usd", 10) + Money("gbp", 10)


def test_multiplying_two_money_values_is_an_error():
    with pytest.raises(TypeError):
        tenner * fiver
