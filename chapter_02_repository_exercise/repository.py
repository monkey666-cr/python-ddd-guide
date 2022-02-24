'''
Author: ChenRun
Date: 2021-12-19 22:21:48
Description: 
'''
import abc

from . import model


class AbstractRepository(abc.ABC):

    @abc.abstractclassmethod
    def add(self, batch: model.Batch):
        raise NotImplementedError

    @abc.abstractclassmethod
    def get(self, reference) -> model.Batch:
        raise NotImplementedError


class SqlRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def get(self, reference) -> model.Batch:
        return self.session.query(model.Batch).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(model.Batch).all()
