from abc import ABC, abstractmethod

from data_models.vote_results import VoteResult


class ReportProcessorInterface(ABC):

    @abstractmethod
    def process_vote_result(self, vote_result: VoteResult) -> None:
        raise NotImplementedError("You must implement the process method")
