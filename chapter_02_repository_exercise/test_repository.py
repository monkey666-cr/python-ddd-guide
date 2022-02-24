'''
Author: ChenRun
Date: 2021-12-19 22:24:42
Description: 
'''

from . import model, repository


def test_repository_can_save_a_batch(session):
    batch = model.Batch("batch1", "RUSTY-SOAPDISH", 100, eta=None)

    repo = repository.SqlRepository(session)
    repo.add(batch)
    session.commit()

    rows = session.execute(
        "SELECT reference, sku, _purchased_quantity, eta FROM 'batches'"
    )
    assert list(rows) == [("batch1", "RUSTY-SOAPDISH", 100, None)]
